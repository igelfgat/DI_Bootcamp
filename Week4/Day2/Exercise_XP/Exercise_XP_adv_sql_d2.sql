SELECT * FROM olympics.city -- id, city_name
SELECT * FROM olympics.games_competitor --id, games_id, person_id, age
SELECT * FROM olympics.competitor_event -- event_id, competitor_id, medal_id
SELECT * FROM olympics.medal -- id, medal_name(4 type)
SELECT * FROM olympics.person -- id, full_name, gender, height, weight
SELECT * FROM olympics.person_region -- person_id, region_id
SELECT * FROM olympics.event -- id, sport_id, event_name
SELECT * FROM olympics.noc_region -- id, noc(сокращение), region_name
SELECT * FROM olympics.games -- id, games_year, games_name, season
SELECT * FROM olympics.games_city -- games_id, city_id
SELECT * FROM olympics.sport -- id, sport_name
/*
Task 1: Find the average age of competitors who have won at least one medal,
grouped by the type of medal they won. Use a correlated subquery to achieve this.
*/
SELECT AVG(age) AS average_age,
	(SELECT medal_name FROM olympics.medal m WHERE m.id = ce.medal_id) AS medal_name
FROM olympics.games_competitor gc
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
WHERE ce.medal_id != 4
GROUP BY ce.medal_id

/*
Task 2: Identify the top 5 regions with the highest number of unique competitors 
who have participated in more than 3 different events. 
Use nested subqueries to filter and aggregate the data.
*/
	
-- Subquery to find competitors who have participated in more than 3 different events
WITH competitors AS (
    SELECT competitor_id
    FROM olympics.competitor_event
    GROUP BY competitor_id
    HAVING COUNT(DISTINCT event_id) > 3
),
-- Subquery to get the region of each competitor
competitor_regions AS (
    SELECT 
        pr.region_id,
        gc.id
    FROM olympics.games_competitor gc
    JOIN olympics.person_region pr 
    ON gc.person_id = pr.person_id
    WHERE gc.id IN (SELECT competitor_id FROM competitors)
),
-- Main query to count unique competitors in each region and get the top 5 regions
region_counts AS (
    SELECT 
        cr.region_id,
        COUNT(DISTINCT cr.id) AS unique_competitors
    FROM competitor_regions cr
    GROUP BY cr.region_id
)
SELECT 
    nr.region_name,
    rc.unique_competitors
FROM region_counts rc
JOIN olympics.noc_region nr 
ON rc.region_id = nr.id
ORDER BY rc.unique_competitors DESC
LIMIT 5;

/*
Task 3: Create a temporary table to store the total number of medals won 
by each competitor and filter to show only those who have won more than 2 medals. 
Use subqueries to aggregate the data.
*/
CREATE TEMPORARY TABLE competitor_medals AS
SELECT 
    competitor_id, 
    medal_id, 
    COUNT(medal_id) AS medal_count 
FROM olympics.competitor_event
WHERE medal_id != 4
GROUP BY 
    competitor_id, 
    medal_id
HAVING 
    COUNT(medal_id) > 2;

/*
Task 4: Use a subquery within a DELETE statement to remove records of competitors 
who have not won any medals from a temporary table created for analysis.
*/
DELETE FROM competitor_medals
WHERE competitor_id IN (
    SELECT 
        competitor_id 
    FROM 
        olympics.competitor_event
    WHERE 
        medal_id = 4
);

SELECT * FROM competitor_medals;

/*Exercise 2: Advanced Data Manipulation And Optimization
Task 1: Update the heights of competitors based on the average height of competitors 
from the same region. Use a correlated subquery within the UPDATE statement.
*/
SELECT * FROM olympics.games_competitor --id, games_id, person_id, age
SELECT * FROM olympics.person -- id, full_name, gender, height, weight
SELECT * FROM olympics.person_region -- person_id, region_id


WITH all_heights AS (SELECT  gc.id,
    p.height,
    pr.region_id
FROM olympics.games_competitor gc
JOIN olympics.person p
ON gc.person_id = p.id
JOIN olympics.person_region pr
ON p.id = pr.person_id),
	
avg_height AS (
	SELECT region_id, ROUND(AVG(height)) AS average_hight
FROM all_heights
WHERE height != 0
GROUP BY region_id
)	

-- UPDATE olympics.person p
-- SET height = (
--         SELECT 
--             ah.average_hight
--         FROM 
--             olympics.person_region pr
--         JOIN 
--             avg_height ah ON pr.region_id = ah.region_id
--         WHERE 
--             pr.person_id = p.id
-- 		LIMIT 1
--     )
-- WHERE 
--     EXISTS (
--         SELECT 1
--         FROM olympics.person_region pr
--         JOIN avg_height ah ON pr.region_id = ah.region_id
--         WHERE pr.person_id = p.id
--     );

UPDATE olympics.person p
SET height = (
    SELECT AVG(p2.height)
    FROM olympics.person p2
    JOIN olympics.person_region pr ON p2.id = pr.person_id
    WHERE pr.region_id = (SELECT pr2.region_id FROM olympics.person_region pr2 WHERE pr2.person_id = p.id)
)
WHERE p.height = 0;
/*
Task 2: Insert new records into a temporary table for competitors who participated 
in more than one event in the same games and list their total number of events 
participated. Use nested subqueries for filtering.
*/

SELECT * FROM olympics.games_competitor --id, games_id, person_id, age
SELECT * FROM olympics.competitor_event -- event_id, competitor_id, medal_id
	
CREATE TEMPORARY TABLE competitors_multiple_events AS
SELECT  ce.competitor_id, gc.games_id, COUNT(ce.event_id) AS total_events 
FROM olympics.games_competitor gc
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
GROUP BY ce.competitor_id, gc.games_id
HAVING
    COUNT(DISTINCT ce.event_id) > 1;

SELECT * FROM competitors_multiple_events;

/*
Task 3: Identify regions where the average number of medals won per competitor is 
greater than the overall average. Use subqueries to calculate and compare averages.
*/
WITH overall AS
	
(SELECT (count(medal_id) / count(DISTINCT competitor_id)) as overall_avg
FROM olympics.competitor_event
WHERE medal_id !=4),
	
regional_avg AS
( SELECT pr.region_id,
	   nr.region_name,
	(count(ce.medal_id) / count(DISTINCT ce.competitor_id)) as region_avg
FROM olympics.person_region as pr
JOIN olympics.noc_region as nr
ON nr.id = pr.region_id
JOIN olympics.person as p
ON p.id = pr.person_id
JOIN olympics.games_competitor as gc
ON gc.person_id = p.id
JOIN olympics.competitor_event as ce
ON gc.id = ce.competitor_id
GROUP BY pr.region_id, nr.region_name)
	
SELECT region_id, region_name, region_avg
FROM regional_avg
WHERE region_avg > (SELECT overall_avg FROM overall);

/*Task 4: Create a temporary table to track competitors’ participation across 
different seasons and identify those who have participated 
in both Summer and Winter games.
*/

SELECT * FROM olympics.games -- id, games_year, games_name, season
	
CREATE TEMPORARY TABLE competitor_seasons AS
SELECT
    gc.person_id,
    g.season
FROM
    olympics.games_competitor gc
JOIN
    olympics.games g ON gc.games_id = g.id
GROUP BY
    gc.person_id, g.season;


SELECT
    cs.person_id
FROM
    competitor_seasons cs
GROUP BY
    cs.person_id
HAVING
    COUNT(DISTINCT cs.season) = 2;

SELECT * FROM competitor_seasons;
-- SELECT * FROM olympics.games_competitor --id, games_id, person_id, age
-- SELECT * FROM olympics.competitor_event -- event_id, competitor_id, medal_id
-- SELECT * FROM olympics.medal -- id, medal_name(4 type)
-- SELECT * FROM olympics.person -- id, full_name, gender, height, weight

-- JOIN METHOD
-- SELECT 
-- 	om.medal_name,
-- 	AVG(gc.age) 
-- FROM olympics.competitor_event ce
-- JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
-- JOIN olympics.medal om ON om.id = ce.medal_id
-- WHERE ce.medal_id != 4
-- GROUP BY ce.medal_id, om.medal_name

SELECT om.medal_name, (
		SELECT AVG(gc.age) FROM olympics.games_competitor gc
		WHERE gc.id IN (
			SELECT ce.competitor_id FROM olympics.competitor_event ce
	        WHERE ce.medal_id = om.id
		)
	) AS average_age
FROM olympics.medal om
WHERE om.id != 4;


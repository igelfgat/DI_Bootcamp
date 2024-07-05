/*Find the NULL elements*/
-- SELECT * FROM customer_support_tickets WHERE "First Response Time" IS NULL; 
--Resolution,First Responce Time, Time to resolution, customer satisfaction ration have NULL value
/* Change column name */
-- SELECT * FROM customer_support_tickets 
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Ticket ID" TO "ticket_id";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Customer Name" TO "customer_name";
-- ALTER TABLE customer_support_tickets	
-- RENAME COLUMN "Customer Email" TO "customer_email";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Customer Age" TO "customer_age";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Customer Gender" TO "customer_gender";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Product Purchased" TO "product_purchased";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Date of Purchase" TO "date_of_purchase";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Ticket Type" TO "ticket_type";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Ticket Subject" TO "ticket_subject";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Ticket Status" TO "ticket_status";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Ticket Priority" TO "ticket_priority";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "Ticket Channel" TO "ticket_channel";
-- ALTER TABLE customer_support_tickets
-- RENAME COLUMN "First Response Time" TO "first_response_time";
SELECT * FROM customer_support_tickets WHERE customer_name = 'James Smith'

SELECT 
    --customer_name,
    customer_email,
    -- customer_age,
    -- customer_gender,
    -- product_purchased,
    -- date_of_purchase,
    -- ticket_type,
    -- ticket_subject,
    -- ticket_status,
    -- ticket_priority,
    -- ticket_channel,
    -- first_response_time,
	COUNT(*)
FROM customer_support_tickets
GROUP BY
    -- customer_name,
    customer_email
    -- customer_age,
    -- customer_gender,
    -- product_purchased,
    -- date_of_purchase,
    -- ticket_type,
    -- ticket_subject,
    -- ticket_status,
    -- ticket_priority,
    -- ticket_channel,
    -- first_response_time
HAVING COUNT(*) > 1
ORDER BY COUNT(*);

/*Delete email duplicate rows*/
-- WITH duplicates AS (
--     SELECT
--         ticket_id,
--         ROW_NUMBER() OVER (PARTITION BY customer_email ORDER BY ticket_id) AS rnum
--     FROM customer_support_tickets 
-- )
-- DELETE FROM customer_support_tickets
-- WHERE ticket_id IN (
--     SELECT ticket_id
--     FROM duplicates
--     WHERE rnum > 1
-- ); 

/* Exercise 2 */
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN customer_name TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN customer_email TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN customer_age TYPE SMALLINT;
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN customer_gender TYPE VARCHAR(20);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN product_purchased TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN date_of_purchase TYPE DATE USING date_of_purchase::DATE;
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN ticket_type TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN ticket_subject TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN ticket_status TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN ticket_priority TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN ticket_channel TYPE VARCHAR(100);
-- ALTER TABLE customer_support_tickets
-- ALTER COLUMN first_response_time TYPE TIMESTAMP USING first_response_time::TIMESTAMP;

-- SELECT * FROM customer_support_tickets 
-- 	WHERE ticket_type != 'Technical issue' 
-- 	AND ticket_type != 'Billing inquiry' 
-- 	AND ticket_type != 'Technical issue'
-- 	AND ticket_type != 'Refund request' 
-- 	AND ticket_type != 'Cancellation request'
-- 	AND ticket_type != 'Product inquiry'

-- UPDATE customer_support_tickets
-- SET customer_gender = CASE
--     WHEN customer_gender IN ('male', 'm', 'man', 'M', 'Male', 'Man') THEN 'Male'
--     WHEN customer_gender IN ('female', 'woman', 'w', 'Female', 'Woman') THEN 'Female'
--     ELSE customer_gender
-- END;


-- UPDATE customer_support_tickets
-- SET ticket_status = CASE
--     WHEN ticket_status IN ('Closed', 'Close', 'c', 'C', 'close', 'closed', 'CLOSED', 'CLOSE') THEN 'Closed'
--     WHEN ticket_status IN ('Open', 'o', 'open', 'OPEN') THEN 'Open'
--     ELSE ticket_status
-- END;

-- UPDATE customer_support_tickets
-- SET ticket_priority = CASE
--     WHEN ticket_priority IN ('High', 'high', 'h', 'H', 'HIGH') THEN 'High'
--     WHEN ticket_priority IN ('Low', 'low', 'l', 'L', 'LOW') THEN 'Low'
--     WHEN ticket_priority IN ('Medium', 'M', 'medium', 'MEDIUM', 'm') THEN 'Medium'
--     WHEN ticket_priority IN ('Critical', 'critical', 'c', 'C', 'CRITICAL') THEN 'Critical'
--     ELSE ticket_priority
-- END;

/* Fill NULL valaue in first_responce_time*/
-- WITH filled_forward AS (
--     SELECT
--         ticket_id,
--         first_response_time,
--         COALESCE(first_response_time, LAG(first_response_time) OVER (ORDER BY ticket_id)) AS filled_forward
--     FROM
--         customer_support_tickets
-- ),
-- filled_backward AS (
--     SELECT
--         ticket_id,
--         first_response_time,
--         filled_forward,
--         COALESCE(first_response_time, LEAD(first_response_time) OVER (ORDER BY ticket_id DESC)) AS filled_backward
--     FROM
--         filled_forward
-- ),
-- final_values AS (
--     SELECT
--         ticket_id,
--         first_response_time,
--         filled_forward,
--         filled_backward,
--         CASE
--             WHEN first_response_time IS NULL THEN
--                 to_timestamp((EXTRACT(EPOCH FROM filled_forward) + EXTRACT(EPOCH FROM filled_backward)) / 2.0)
--             ELSE
--                 first_response_time
--         END AS new_value
--     FROM
--         filled_backward
-- )
-- UPDATE customer_support_tickets AS cst
-- SET
--     first_response_time = final_values.new_value
-- FROM
--     final_values
-- WHERE
--     cst.ticket_id = final_values.ticket_id
--     AND cst.first_response_time IS NULL;

/* Exercies 3 */
-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     employee_name VARCHAR(50),
--     department_id INT
-- );
-- INSERT INTO employees (employee_id, employee_name, department_id) VALUES
-- (1, 'Alice', 101),
-- (2, 'Bob', NULL),
-- (3, 'Charlie', 102),
-- (4, 'Dave', 103),
-- (5, 'Eve', NULL),
-- (6, 'Frank', 104),
-- (7, 'Grace', 105),
-- (8, 'Hank', NULL),
-- (9, 'Ivy', 102),
-- (10, 'Jack', 101),
-- (11, 'Ken', NULL),
-- (12, 'Laura', 103),
-- (13, 'Mallory', 104),
-- (14, 'Niaj', 105),
-- (15, 'Oscar', NULL),
-- (16, 'Peggy', 101),
-- (17, 'Quentin', 102),
-- (18, 'Rick', NULL),
-- (19, 'Steve', 103),
-- (20, 'Trent', 104),
-- (21, 'Uma', 105),
-- (22, 'Vince', NULL),
-- (23, 'Walter', 101),
-- (24, 'Xander', 102),
-- (25, 'Yvonne', 103),
-- (26, 'Zara', 104),
-- (27, 'Alan', NULL),
-- (28, 'Betty', 101),
-- (29, 'Carl', 102),
-- (30, 'Diana', NULL),
-- (31, 'Ed', 103),
-- (32, 'Fiona', 104),
-- (33, 'George', 105),
-- (34, 'Holly', NULL),
-- (35, 'Ian', 101),
-- (36, 'Jane', 102),
-- (37, 'Kyle', 103),
-- (38, 'Liam', NULL),
-- (39, 'Mia', 104),
-- (40, 'Nina', 105),
-- (41, 'Owen', NULL),
-- (42, 'Paula', 101),
-- (43, 'Quincy', 102),
-- (44, 'Ray', 103),
-- (45, 'Sara', 104),
-- (46, 'Tom', 105),
-- (47, 'Ursula', NULL),
-- (48, 'Victor', 101),
-- (49, 'Wendy', 102),
-- (50, 'Xavier', NULL);
-- CREATE TABLE departments (
--     department_id INT PRIMARY KEY,
--     department_name VARCHAR(50)
-- );
-- INSERT INTO departments (department_id, department_name) VALUES
-- (101, 'Sales'),
-- (102, 'Marketing'),
-- (103, 'Engineering'),
-- (104, 'Human Resources'),
-- (105, 'IT Support'),
-- (106, 'Finance'),
-- (107, 'Operations'),
-- (108, 'R&D'),
-- (109, 'Customer Service'),
-- (110, 'Legal'),
-- (111, 'Administration'),
-- (112, 'Procurement'),
-- (113, 'Quality Assurance'),
-- (114, 'Production'),
-- (115, 'Logistics'),
-- (116, 'Maintenance'),
-- (117, 'Security'),
-- (118, 'Public Relations'),
-- (119, 'Research'),
-- (120, 'Strategy');

select employee_name,department_name from employees e
LEFT JOIN departments d ON e.department_id = d.department_id
/* Modify the query to include a condition that highlights:
		Employees who do not belong to any department.
		Departments that do not have any employees assigned.*/
WHERE department_name IS NULL;


SELECT 
    d.department_name,
    COUNT(e.employee_id) AS count_employees 
FROM 
    departments d 
LEFT JOIN 
    employees e ON e.department_id = d.department_id
GROUP BY 
    d.department_name
HAVING 
    COUNT(e.employee_id) = 0;

/* Exercise 4: Consolidating Employee And Department Data With FULL JOIN

Objective
Use a FULL JOIN to create a comprehensive list of all employees and their respective departments, 
including those without matches on either side.*/

SELECT e.employee_id, e.employee_name, d.department_id, d.department_name FROM departments d
FULL JOIN employees e ON e.department_id = d.department_id


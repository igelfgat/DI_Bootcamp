/*
select * from olist_customers_dataset -- customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state
select * from olist_geolocation_dataset -- geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state
select * from olist_order_items_dataset -- order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value
select * from olist_order_payments_dataset -- order_id, payment_sequential, payment_type, payment_installments, payment_value
select * from olist_order_reviews_dataset -- review_id, order_id, review_score, review_comment_title, review_comment_message
select * from olist_orders_dataset -- order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date
select * from olist_products_dataset -- product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g,...
select * from olist_sellers_dataset -- seller_id, seller_zip_code_prefix, seller_city, seller_state
select * from product_category_name_translation -- product_category_name, product_category_name_english
*/
/*3. Query 1: Count and Percentage of Orders Purchased in Jan 2018 with 5 Review Score

Write and execute a SQL query to count the number of orders purchased in January 2018 
that have a review score of 5 and calculate the percentage of such orders.*/
/* Change text to TIMESTAMP*/
-- ALTER TABLE olist_orders_dataset
-- ALTER COLUMN order_purchase_timestamp TYPE TIMESTAMP USING order_purchase_timestamp::TIMESTAMP;

SELECT (orders_with_score_5 * 100.0 / total_orders) AS percentage_of_orders_with_score_5
FROM (
  SELECT COUNT(*) AS total_orders
  FROM olist_orders_dataset
  WHERE EXTRACT(YEAR FROM order_purchase_timestamp) = 2018 
    AND EXTRACT(MONTH FROM order_purchase_timestamp) = 1
	),
(
  SELECT COUNT(*) AS orders_with_score_5
  FROM olist_orders_dataset od
  LEFT JOIN olist_order_reviews_dataset ord ON od.order_id = ord.order_id
  WHERE EXTRACT(YEAR FROM order_purchase_timestamp) = 2018 
    AND EXTRACT(MONTH FROM order_purchase_timestamp) = 1 
    AND review_score = 5
);

/*Query 2: Customer Purchase Trend Year-on-Year

Write and execute a SQL query to analyze the customer purchase trend year-on-year.*/
SELECT
  EXTRACT(YEAR FROM o.order_purchase_timestamp) AS order_year,
  SUM(p.payment_value) AS total_sales_amount,
  COUNT(DISTINCT o.order_id) AS total_orders,
  COUNT(DISTINCT o.customer_id) AS total_customers
FROM
  olist_orders_dataset o
JOIN
  olist_order_items_dataset i ON o.order_id = i.order_id
JOIN
  olist_order_payments_dataset p ON o.order_id = p.order_id
WHERE
  o.order_status = 'delivered' -- Only consider delivered orders
GROUP BY
  EXTRACT(YEAR FROM o.order_purchase_timestamp)
ORDER BY
  order_year;


/*Query 3: Average Order Values of Customers
Write and execute a SQL query to calculate the average order values of customers.*/
SELECT o.customer_id, AVG(p.payment_value) AS average_order_value FROM olist_orders_dataset o
JOIN olist_order_payments_dataset p ON o.order_id = p.order_id
GROUP BY o.customer_id

/*Query 4: Top 5 Cities with Highest Revenue from 2016 to 2018
Write and execute a SQL query to find the top 5 cities with the highest revenue from 2016 to 2018.*/
SELECT 
	COUNT(oi.seller_id) AS count_sellers_in_city, 
	s.seller_city, 
	SUM(oi.price) AS revenue_by_seller_id 
FROM olist_order_items_dataset oi
JOIN olist_sellers_dataset s ON oi.seller_id = s.seller_id
JOIN olist_orders_dataset o ON o.order_id = oi.order_id
WHERE EXTRACT(YEAR FROM order_purchase_timestamp) >= 2016 AND EXTRACT(YEAR FROM order_purchase_timestamp) <= 2018
GROUP BY s.seller_city
ORDER BY revenue_by_seller_id DESC 
LIMIT 5;

/*Query 5: State Wise Revenue Table Between 2016 to 2018
Write and execute a SQL query to create a state-wise revenue table between 2016 to 2018.*/

SELECT 
	EXTRACT(YEAR FROM o.order_purchase_timestamp) AS order_year,
	s.seller_state, 
	SUM(oi.price) AS revenue 
FROM olist_sellers_dataset s
JOIN olist_order_items_dataset oi ON oi.seller_id = s.seller_id 
JOIN olist_orders_dataset o ON o.order_id = oi.order_id
WHERE 
	EXTRACT(YEAR FROM order_purchase_timestamp) >= 2016 AND 
	EXTRACT(YEAR FROM order_purchase_timestamp) <= 2018
GROUP BY 
	EXTRACT(YEAR FROM o.order_purchase_timestamp),
	s.seller_state
ORDER BY
  order_year,
  revenue DESC;

/*Query 6: Top Successful Sellers in Terms of Goods Sold, Revenue, and Customer Count
Write and execute a SQL query to identify the top successful sellers 
in terms of the number of goods sold, total revenue, customer count, and sellers with the highest 5-star ratings.*/

SELECT 
	oi.seller_id, 
	COUNT(DISTINCT o.customer_id) AS customer_count, 
	COUNT(oi.order_id) AS num_of_goods_sold, 
	SUM(oi.price) AS total_revenue,
	SUM(CASE WHEN r.review_score = 5 THEN 1 ELSE 0 END) AS count_5_star_rating
FROM olist_order_items_dataset oi
JOIN olist_orders_dataset o ON o.order_id = oi.order_id
JOIN olist_order_reviews_dataset r ON o.order_id = r.order_id
WHERE 
  o.order_status IN ('delivered', 'shipped', 'invoiced') AND r.review_score = 5
GROUP BY oi.seller_id 
ORDER BY count_5_star_rating DESC

	
/*Query 7: Delivery Success Rate Across States
Write and execute a SQL query to calculate the delivery success rate across different states.*/

SELECT
  c.customer_state,
  COUNT(CASE WHEN o.order_status = 'delivered' THEN 1 END) AS delivered_orders,
  COUNT(o.order_id) AS total_orders,
  ROUND((COUNT(CASE WHEN o.order_status = 'delivered' THEN 1 END) * 1.0 / COUNT(o.order_id)) * 100, 2) AS delivery_success_rate
FROM
  olist_orders_dataset o
JOIN
  olist_customers_dataset c ON o.customer_id = c.customer_id
GROUP BY
  c.customer_state
ORDER BY
  delivery_success_rate DESC;

/*Query 8: Preferred Form of Payment for Different Categories
Write and execute a SQL query to find the preferred form of payment for different product categories.*/
-- Show all forms of payment 
SELECT p.product_category_name, 
	op.payment_type, 
	COUNT(op.payment_type) AS payment_count
FROM olist_order_items_dataset oi
JOIN olist_products_dataset p ON p.product_id = oi.product_id
JOIN olist_order_payments_dataset op ON oi.order_id = op.order_id
GROUP BY p.product_category_name, op.payment_type
ORDER BY 
  p.product_category_name, 
  payment_count DESC;
-- The preferred form of payment
WITH PaymentCounts AS (
  SELECT 
    p.product_category_name, 
    op.payment_type, 
    COUNT(op.payment_type) AS payment_count,
    ROW_NUMBER() OVER (PARTITION BY p.product_category_name ORDER BY COUNT(op.payment_type) DESC) AS rn
  FROM 
    olist_order_items_dataset oi
  JOIN 
    olist_products_dataset p ON p.product_id = oi.product_id
  JOIN 
    olist_order_payments_dataset op ON oi.order_id = op.order_id
  GROUP BY 
    p.product_category_name, 
    op.payment_type
)
SELECT 
  product_category_name, 
  payment_type, 
  payment_count
FROM 
  PaymentCounts
WHERE 
  rn = 1
ORDER BY 
  product_category_name;


/*Query 9: Distance Between Cities
Write and execute a SQL query to calculate the distance between cities.*/
select * from olist_geolocation_dataset -- geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state


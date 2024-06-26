-- Get a list of all the languages, from the language table.
--SELECT name FROM language

--Get a list of all films joined with their languages – select the following details : film title, description, and language name.

-- SELECT title, description, name FROM film f
-- JOIN language l 
-- ON f.language_id = l.language_id

--Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

-- SELECT title, description, name FROM film f
-- RIGHT JOIN language l 
-- ON f.language_id = l.language_id

--Create a new table called new_film with the following columns : id, name. Add some new films to the table.

-- CREATE TABLE new_film (
-- 	new_film_id serial primary key,
-- 	name varchar(200)
-- );

-- INSERT INTO new_film(name) VALUES(
-- 	'Spaceman'
-- );
-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- create table customer_review(
-- review_id serial primary key,
-- film_id int,
-- language_id int,
-- title varchar(255),
-- score int check (score >= 1 AND score <= 10),
-- review_text text,
-- last_update date,
-- foreign key (film_id) references new_film(new_film_id) on delete cascade,	
-- foreign key (language_id) references language(language_id)	
-- );

--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update) VALUES(
-- 	2,
-- 	(SELECT language_id from language where name='Italian'),
-- 	'The title of the review about the first film',
-- 	8,
-- 	'Some text about the film. How great is it!',
-- 	'2024-01-25'
-- );

-- INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update) VALUES(
-- 	1,
-- 	(SELECT language_id from language where name='English'),
-- 	'The title of the review about the second film',
-- 	8,
-- 	'Some text about the film. How great or bad is it!',
-- 	'2024-01-20'
-- );

--Delete a film that has a review from the new_film table, what happens to the customer_review table?
--DELETE FROM new_film WHERE new_film_id = 2;
-- Delete it also from customer_review table

--Exercise 2 : DVD Rental
--Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- update film
-- set language_id = (select language_id from language where name = 'French')
-- where film_id = 1;

--Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

--address_id. We have to check if this foreign keys exist in the main table(address).

--We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

--drop table customer_review
--Dropping a table is easy step, but you should check that no other tables depend on it. 
--In our case, it’s a simple operation since we know its structure and dependencies.

--Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

--select count(*) from rental where return_date is null

--Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- select f.title, f.rental_rate
-- from rental r
-- join inventory i on r.inventory_id = i.inventory_id
-- join film f on i.film_id = f.film_id
-- where r.return_date is null
-- order by f.rental_rate desc
-- limit 30;

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- select f.title
-- from film f
-- join film_actor fa on f.film_id = fa.film_id
-- join actor a on fa.actor_id = a.actor_id
-- where f.description ilike '%sumo wrestler%'
-- and a.first_name = 'Penelope'
-- and a.last_name = 'Monroe';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- select title
-- from film
-- where length < 60
-- and rating = 'R'
-- and description ilike '%documentary%';

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- select f.title
-- from rental r
-- join customer c on r.customer_id = c.customer_id
-- join inventory i on r.inventory_id = i.inventory_id
-- join film f on i.film_id = f.film_id
-- where c.first_name = 'Matthew'
-- and c.last_name = 'Mahan'
-- and r.return_date between '2005-07-28' and '2005-08-01'
-- and f.rental_rate > 4.00;

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
select f.title
from rental r
join customer c on r.customer_id = c.customer_id
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
where c.first_name = 'Matthew'
and c.last_name = 'Mahan'
and (f.title ilike '%boat%' or f.description ilike '%boat%')
order by f.replacement_cost desc
limit 1;
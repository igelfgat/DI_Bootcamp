--Part I
-- create table customer(
-- id serial primary key, 
-- first_name varchar (50) not null,
-- last_name varchar (50) not null
-- );

-- create table customer_profile(
-- id serial primary key, 
-- isLoggedIn bool DEFAULT false,
-- customer_id int references customer(id) on delete cascade unique
-- );

-- insert into customer(first_name, last_name) values 
-- 	('John', 'Doe'), 
-- 	('Jerome', 'Lalu'),
-- 	('Lea', 'Rive');

-- insert into customer_profile (isLoggedIn, customer_id) values 
-- 	(True, (select id from customer where first_name='John')),
-- 	(False, (select id from customer where first_name='Jerome'))


-- Use the relevant types of Joins to display:
-- The first_name of the LoggedIn customers
	
-- select first_name from customer
-- left join customer_profile
-- on customer.id = customer_profile.customer_id
-- where isLoggedIn = True

--All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.

-- select first_name,isLoggedIn from customer
-- left join customer_profile
-- on customer.id = customer_profile.customer_id

--The number of customers that are not LoggedIn

-- select count(*) from customer
-- left join customer_profile
-- on customer.id = customer_profile.customer_id
-- where isLoggedIn = False or isLoggedIn is null

-- create table book(
-- 	book_id serial primary key, 
--  title varchar (200) not null,
-- 	author varchar (200) not null
-- );

-- insert into book(title, author) values 
-- 	('Alice In Wonderland', 'Lewis Carroll'), 
-- 	('Harry Potter', 'J.K Rowling'),
-- 	('To kill a mockingbird', 'Harper Lee');

-- create table student(
-- 	student_id serial primary key, 
--  	name varchar (200) not null unique,
-- 	age int check (age <= 15)
-- );

-- insert into student(name, age) values 
-- 	('John', 12), 
-- 	('Lera', 11),
-- 	('Patrick', 10),
-- 	('Bob', 14);

-- create table library(
-- 	book_fk_id INTEGER,
--     student_fk_id INTEGER,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id),
--     FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- insert into library(book_fk_id, student_fk_id, borrowed_date) values(
-- 	(select book_id from book where title = 'Alice In Wonderland'),
-- 	(select student_id from student where name = 'John'),
-- 	'2022-02-15'
-- );

-- insert into library(book_fk_id, student_fk_id, borrowed_date) values(
-- 	(select book_id from book where title = 'To kill a mockingbird'),
-- 	(select student_id from student where name = 'Bob'),
-- 	'2021-03-03'
-- );

-- insert into library(book_fk_id, student_fk_id, borrowed_date) values(
-- 	(select book_id from book where title = 'Alice In Wonderland'),
-- 	(select student_id from student where name = 'Lera'),
-- 	'2021-05-23'
-- );

-- insert into library(book_fk_id, student_fk_id, borrowed_date) values(
-- 	(select book_id from book where title = 'Harry Potter'),
-- 	(select student_id from student where name = 'Bob'),
-- 	'2021-08-12'
-- );

-- Display the data
-- Select all the columns from the junction table

--select * from library

--Select the name of the student and the title of the borrowed books

-- select name, title from student s
-- join library l
-- on s.student_id = l.student_fk_id
-- join book b
-- on b.book_id = l.book_fk_id;

--Select the average age of the children, that borrowed the book Alice in Wonderland

-- select avg(s.age) as average_age
-- from library l
-- join book b on l.book_fk_id = b.book_id
-- join student s on l.student_fk_id = s.student_id
-- where b.title = 'Alice In Wonderland';

--delete from Student where name = 'Bob';
select * from library;



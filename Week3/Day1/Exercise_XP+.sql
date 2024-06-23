/*create table students(
	id serial primary key,
	last_name varchar(30),
	first_name varchar(30),
	birthdate date
);*/

/*INSERT INTO students (first_name, last_name, birthdate) VALUES
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03'),
('Ilya', 'Gelfgat', '1999-03-21');*/
--select * from students;
--select first_name, last_name from students;
--select first_name, last_name from students where id = 2
--select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc'
--select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc'
--select first_name, last_name from students where first_name LIKE '%a%'
--select first_name, last_name from students where first_name ILIKE 'a%'
--select first_name, last_name from students where first_name LIKE '%a'
--select first_name, last_name from students where first_name LIKE '%a_'
--select first_name, last_name from students where id = 1 or id = 3
select * from students where birthdate >= '2000-01-01'
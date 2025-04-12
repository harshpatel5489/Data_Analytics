use assesment;

create table question1(
worker_id int unique not null,
first_name varchar (50),
last_name varchar (50),
salary int,
joinning_date text not null,
department varchar(40) not null
);


select * from question1;
insert into question1 values (1,'monika','arora',100000,'02/20/2014 09:00','HR');
insert into question1 values (2,'niharika','verma',80000,'06/20/2014 09:00','ADMIN');
insert into question1 values (3,'vishal','sighal',300000,'02/20/2014 09:00','HR');
insert into question1 values (4,'amitabh','sigh',100000,'02/20/2014 09:00','ADMIN');
insert into question1 values (5,'vivek','bhati',500000,'06/11/2014 09:00','ADMIN');
insert into question1 values (6,'vipul','diwan',200000,'06/11/2014 09:00','ACCOUNT');
insert into question1 values (7,'satish','kumar',75000,'01/20/2014 09:00','ACCOUNT');
insert into question1 values (8,'geetika','chauhan',90000,'04/11/2014 09:00','ADMIN');

-- 1. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAMEAscending and DEPARTMENT Descending.

select * from question1 order by first_name asc , department desc ;
select * from question1 order by department desc ;

-- 2.Write an SQL query to print details for Workers with the first names “Vipul” and “Satish”the Worker table.

select * from question1 where worker_id in (6,7);

-- 3. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets. 

select * from question1 where first_name like '_____h';

-- 4. Write an SQL query to print details of the Workers whose SALARY lies between 200000 to 400000. 

select * from question1 where salary > 200000 and salary <= 400000;

-- 5. Write an SQL query to fetch duplicate records having matching data in some fields of a table. 

SELECT Worker_id,FIRST_NAME,LAST_NAME,SALARY,joinning_date,DEPARTMENT, COUNT(*)
FROM question1
GROUP BY Worker_id,FIRST_NAME,LAST_NAME,SALARY,joinning_date,DEPARTMENT
HAVING COUNT(*) > 1;

-- 6. Write an SQL query to show the top 6 records of a table. 

select * from question1 limit 6;

-- 7. Write an SQL query to fetch the departments that have less than five people in them.

select department from question1 group by department having count(worker_id) < 5;

-- 8. Write an SQL query to show all departments along with the number of people in there.

select department,count(*) as number_people from question1 group by department ;

-- 9. Write an SQL query to print the name of employees having the highest salary in each department.

select first_name,department,salary from question1 e1
 where salary = (select
max(salary) from question1 e2 where e1.department = e2.department ) order by department;


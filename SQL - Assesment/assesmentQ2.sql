create table question2(
stdID int not null unique,
stdName varchar(20),
sex varchar (20),
percentage int not null,
class int,
sec varchar(5),
Stream varchar(20),
DOB varchar(25) not null
);

update question2 set DOB = date_format(dob, '%m/%d/%y');

insert into question2 values(1001,'Surekha joshi','Female',82,12,'A','Science','03/08/1998');
insert into question2 values(1002,'Mahi Agarawal','Female',56,11,'C','Commerce','11/23/2008');
insert into question2 values(1003,'Sanam Verma','Male',82,12,'C','Commerce','06/29/2006');
insert into question2 values(1004,'ronit kumar','Male',63,11,'C','Commerce','11/5/1997');
insert into question2 values(1005,'Dipesh Pulkit','Male',78,11,'B','Science','14/09/2003');
insert into question2 values(1006,'jahanvi puri','female',60,11,'B','Commerce','11/07/2003');
insert into question2 values(1007,'Sanam kumar','male',23,12,'F','Commerce','3/08/1998');	
insert into question2 values(1008,'Sahil saras','male',56,11,'C','Commerce','11/07/2008');
insert into question2 values(1009,'akshara agrawal','female',72,12,'B','Commerce','10/01/1996');
insert into question2 values(1010,'stuti mishra','female',40,11,'F','Science','11/23/2008');
insert into question2 values(1011,'harsh agrawal','male',42,11,'c','Science','03/08/1998');
insert into question2 values(1012,'nikunj agrawal','male',49,12,'c','Commerce','28/06/1998');
insert into question2 values(1013,'akriti saxena','female',89,12,'a','Science','11/23/2008');
insert into question2 values(1014,'tani rastogi','female',82,12,'a','Science','11/07/2003');

-- Q-1 To display all the records form STUDENT table. 

SELECT * FROM question2 ;  

-- Q-2 2. To display any name and date of birth from the table STUDENT.

select stdname,DOB from question2;

-- Q-3 3. To display all students record where percentage is greater of equal to 80 FROM student table.

select * from question2 where percentage >=80;

-- Q-4. To display student name, stream and percentage where percentage of student is more than 80.

select stdname,stream,percentage from question2 where percentage >=80 ;

-- Q-5. 5. To display all records of science students whose percentage is more than 75 form student table.

select * from question2 where stream = 'science' and percentage > 75;
-- Create a new database named 'assignment1'
create database assignment1;

-- Select and use the 'assignment1' database
use assignment1;

-- Create a table to store company information
create table company(
    company_id int primary key,              -- Unique identifier for each company
    company_name varchar(45),                -- Name of the company
    street varchar(45),                      -- Street address of the company
    city varchar(45),                        -- City where the company is located
    state varchar(45),                       -- State where the company is located
    zip varchar(10)                          -- ZIP code of the company's address
);

-- Insert sample data into the 'company' table
insert into company (company_id, company_name, street, city, state, zip)
values
(1, 'Urban Outfitters', '5000 South Broad St', 'Philadelphia', 'PA', '19112'),
(2, 'Apple Inc.', '1 Infinite Loop', 'Cupertino', 'CA', '95014'),
(3, 'Microsoft', '1 Microsoft Way', 'Redmond', 'WA', '98052'),
(4, 'Google', '1600 Amphitheatre Parkway', 'Mountain View', 'CA', '94043'),
(5, 'Amazon', '410 Terry Ave N', 'Seattle', 'WA', '98109');

-- Create a table to store contact person information related to companies
create table contact(
    contact_id int primary key,              -- Unique identifier for each contact
    company_id int,                          -- References the company this contact belongs to
    first_name varchar(45),                  -- First name of the contact
    last_name varchar(45),                   -- Last name of the contact
    street varchar(45),                      -- Contact's street address
    city varchar(45),                        -- Contact's city
    state varchar(2),                        -- Contact's state (2-letter code)
    zip varchar(10),                         -- Contact's ZIP code
    ismain boolean,                          -- Indicates if this is the main contact
    Email varchar(45),                       -- Email address of the contact
    Phone varchar(12),                       -- Phone number of the contact
    foreign key (company_id) references company (company_id) -- Link to the company table
);

-- Insert sample data into the 'contact' table
insert into contact (contact_id, company_id, first_name, last_name, street, city, state, zip, ismain, Email, Phone)
values
(1, 1, 'Alice', 'Johnson', '5000 South Broad St', 'Philadelphia', 'PA', '19112', true, 'alice.johnson@urbanoutfitters.com', '215-555-1234'),
(2, 2, 'Bob', 'Smith', '1 Infinite Loop', 'Cupertino', 'CA', '95014', true, 'bob.smith@apple.com', '408-555-5678'),
(3, 3, 'Charlie', 'Davis', '1 Microsoft Way', 'Redmond', 'WA', '98052', false, 'charlie.davis@microsoft.com', '425-555-9876'),
(4, 4, 'Dana', 'Lee', '1600 Amphitheatre Parkway', 'Mountain View', 'CA', '94043', true, 'dana.lee@google.com', '650-555-2345'),
(5, 5, 'Eva', 'Martin', '410 Terry Ave N', 'Seattle', 'WA', '98109', false, 'eva.martin@amazon.com', '206-555-8765');

-- Create a table to store employee information
create table employee(
    employee_id int primary key,             -- Unique identifier for each employee
    firstname varchar(45),                   -- First name of the employee
    lastname varchar(45),                    -- Last name of the employee
    salary decimal(10,2),                    -- Salary of the employee
    HireDate date,                           -- Hiring date
    jobTitle varchar(45),                    -- Job title of the employee
    Email varchar(45),                       -- Email address of the employee
    Phone varchar(12)                        -- Phone number of the employee
);

-- Insert sample data into the 'employee' table
insert into employee (employee_id, firstname, lastname, salary, HireDate, jobTitle, Email, Phone)
values
(1, 'Dianne', "Connor's", 75000.00, '2022-01-15', 'Software Engineer', 'Dianne@microsoft.com', '425-555-1234'),
(2, 'Sarah', 'Lee', 85000.00, '2020-03-10', 'Product Manager', 'sarah.lee@apple.com', '408-555-4321'),
(3, 'Jack', 'Lee', 95000.00, '2021-06-20', 'Data Scientist', 'Jackn@google.com', '650-555-5678'),
(4, 'Emily', 'Davis', 70000.00, '2023-09-01', 'Marketing Specialist', 'emily.davis@amazon.com', '206-555-8765'),
(5, 'Lesley', 'Wilson', 65000.00, '2022-12-15', 'UX Designer', 'david.wilson@urbanoutfitters.com', '215-555-6789');

-- Show all data from the 'employee' table
select * from employee;

-- Create a table to track interactions between employees and contacts
create table contact_employee(
    contact_employee_id int primary key,     -- Unique ID for each interaction
    contact_id int,                          -- Foreign key to the contact table
    employee_id int,                         -- Foreign key to the employee table
    contactDate date,                        -- Date of contact
    description varchar(100)                 -- Description of the interaction
);

-- Insert data into 'contact_employee' table
insert into contact_employee (contact_employee_id, contact_id, employee_id, contactDate, description)
values
(1, 1, 1, '2023-01-10', 'Initial meeting with Alice from Urban Outfitters to discuss collaboration opportunities.'),
(2, 2, 2, '2022-11-25', 'Follow-up email with Bob from Apple regarding product feedback.'),
(3, 3, 3, '2023-03-15', 'Conference call with Charlie from Microsoft about data analysis project.'),
(4, 4, 4, '2023-02-20', 'Interview with Dana from Google about marketing strategy.'),
(5, 5, 5, '2023-04-05', 'Product launch planning with Eva from Amazon for new features.');

-- (Optional) Add foreign keys explicitly for 'contact_employee' table
alter table contact_employee add foreign key (contact_id) references contact(contact_id);
alter table contact_employee add foreign key (employee_id) references employee(employee_id);

-- Update phone number for the employee named 'Lesley'
update employee set Phone = '215-555-8800' where firstname = 'Lesley';

-- Update company name from 'Urban Outfitters, Inc.' to 'Urban Outfitters'
-- (Note: This won't change anything unless such a record exists)
update company set company_name = 'Urban Outfitters' where company_name = 'Urban Outfitters, Inc.';

-- Delete records from 'contact_employee' for Dianne and Jack using IN + OR
delete from contact_employee 
where employee_id IN (
    select employee_id from employee 
    where (firstname = 'Dianne' and lastname = "Connor's") 
       or (firstname = 'Jack' and lastname = 'Lee')
);

-- Select first and last names of contacts who work for 'Microsoft'
select e.first_name, e.last_name 
from contact e 
join company c on e.company_id = c.company_id 
where company_name = 'Microsoft';


/*  8) What is the significance of “%” and “_” operators in the LIKE statement?

%: Represents zero or more characters.
Example: SELECT * FROM customers WHERE name LIKE 'A%' will match all names that start with 'A'.
_: Represents exactly one character.
Example: SELECT * FROM customers WHERE name LIKE 'A_n' will match names like 'Ann', 'Anx', etc., where there is exactly one character between 'A' and 'n'.

9) Explain normalization in the context of databases.
Normalization is the process of organizing data in a database to minimize redundancy and dependency.

The process involves dividing a database into multiple tables and defining relationships between them. It follows several "normal forms" (1NF, 2NF, 3NF, etc.), each with specific rules to ensure proper structure and data integrity.

10) What does a join in MySQL mean?
In MySQL, a JOIN is a way to combine rows from two or more tables based on a related column between them. It allows you to retrieve data from multiple tables in a single query, helping to represent relationships between them.

For example, if you have a customers table and an orders table, a JOIN can be used to display the customer names along with their order details.

11) What do you understand about DDL, DCL, and DML in MySQL?
DDL (Data Definition Language): Refers to SQL commands that define the structure of the database, such as creating, altering, or deleting tables.

Examples: CREATE, ALTER, DROP.
DCL (Data Control Language): Involves commands that control access to data in the database, specifically permissions and security.

Examples: GRANT, REVOKE.
DML (Data Manipulation Language): Includes commands that manipulate data in the database, such as inserting, updating, or deleting data.

Examples: INSERT, UPDATE, DELETE.

12) What is the role of the MySQL JOIN clause in a query, and what are some common types of joins?
The JOIN clause in MySQL allows you to combine rows from two or more tables based on a related column between them. 

Common types of joins:

INNER JOIN: Returns records that have matching values in both tables.

Example: Get customers who have placed orders.
LEFT JOIN (or LEFT OUTER JOIN): Returns all records from the left table and the matched records from the right table. If no match, NULL values are returned for the right table.

Example: Get all customers and their orders (if any).
RIGHT JOIN (or RIGHT OUTER JOIN): Similar to LEFT JOIN but returns all records from the right table and matching records from the left table.

FULL JOIN (or FULL OUTER JOIN): Returns all records when there is a match in either left or right table (not supported in MySQL, but can be simulated).
*/

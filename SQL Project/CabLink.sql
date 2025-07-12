-- Create a new database named 'project'
CREATE DATABASE project;

-- Use the newly created database
USE project;

-- Create 'driver' table to store driver details
CREATE TABLE driver (
  driver_id INT PRIMARY KEY,                     -- Unique ID for each driver
  driver_name VARCHAR(255),                      -- Name of the driver
  age INT,                                       -- Driver's age
  vehicle_type VARCHAR(255),                     -- Type of vehicle (e.g., SUV, Sedan)
  charge INT,                                    -- Charge per ride
  availability VARCHAR(255)                      -- Driver availability (Available/Unavailable)
);

-- Create 'passenger' table to store ride details
CREATE TABLE passenger (
  passenger_id INT PRIMARY KEY,                  -- Unique ID for each passenger/ride
  starting_point VARCHAR(255),                   -- Ride starting location
  ending_point VARCHAR(255),                     -- Ride ending location
  price INT,                                     -- Fare for the ride
  driver_name VARCHAR(255),                      -- Name of driver (for display)
  driver_id INT,                                 -- Driver assigned to this ride
  FOREIGN KEY(driver_id) REFERENCES driver(driver_id)  -- Linking to driver table
);

-- 1. All rides with driver and passenger info
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id;

-- 2. Rides by available drivers only
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE availability = 'Available';

-- 3. Rides with vehicle type 'SUV'
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE vehicle_type = 'SUV';

-- 4. Rides starting from 'Delhi'
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE starting_point = 'Delhi';

-- 5. Rides from 'Mumbai' to 'Pune'
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE starting_point = 'Mumbai' AND ending_point = 'Pune';

-- 6. Rides with Electric vehicles
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE vehicle_type = 'Electric';

-- 7. Passengers who paid more than ₹500
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE price > 500;

-- 8. Rides by drivers older than 35
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE age > 35;

-- 9. Rides with driver charge less than ₹12
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE charge < 12;

-- 10. Total earnings for each driver
SELECT driver.driver_name, SUM(price) AS total_earnings
FROM driver
JOIN passenger ON driver.driver_id = passenger.driver_id
GROUP BY driver.driver_name;

-- 11. Rides by unavailable drivers
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE availability = 'Unavailable';

-- 12. Rides from cities starting with 'P'
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
WHERE starting_point LIKE 'P%';

-- 13. Drivers with more than 1 ride
SELECT driver.driver_name, COUNT(*) AS ride_count
FROM driver
JOIN passenger ON driver.driver_id = passenger.driver_id
GROUP BY driver.driver_name
HAVING ride_count > 1;

-- 14. Ride with highest fare
SELECT * 
FROM driver 
JOIN passenger ON driver.driver_id = passenger.driver_id
ORDER BY price DESC
LIMIT 1;

-- 15. All drivers including those who have no rides (LEFT JOIN)
SELECT * 
FROM driver 
LEFT JOIN passenger ON driver.driver_id = passenger.driver_id;

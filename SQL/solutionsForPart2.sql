
---------------------------------------------------------------------------------------------------------------------------------------
-- Question 1: 
---------------------------------------------------------------------------------------------------------------------------------------


-- Creating a table 
CREATE TABLE countries (
    country VARCHAR(50) PRIMARY KEY
);

-- Inserting data for countries
INSERT INTO countries (country)
VALUES 
    ('India'),
    ('Pakistan'),
    ('Australia'),
    ('England');


/* 
I utilized cross join as a brute force approach to solve this problem by comparing two countries in lexographical order
from all possible combinations of n*n 
*/

select c1.country, c2.country
	from countries c1, countries c2 where c1.country < c2.country;
    
-- to furter optimize i used INNER JOIN with a condition that filters out unwanted pairs and immediate reverse pairs as well
Select c1.country, c2.country
	from countries c1 JOIN countries c2 ON c1.country < c2.country



---------------------------------------------------------------------------------------------------------------------------------------
-- Question2
---------------------------------------------------------------------------------------------------------------------------------------



-- Creating a table 

CREATE TABLE students_results (
    id INT PRIMARY KEY,
    studentname VARCHAR(50),
    subjectname VARCHAR(50),
    marks INT
);

-- inserting records into table

INSERT INTO students_results (id, studentname, subjectname, marks) VALUES
(1, 'Jyoti', 'Maths', 90),
(2, 'Hritik', 'Maths', 85),
(3, 'Arun', 'Maths', 90),
(4, 'Jyoti', 'English', 70),
(5, 'Arun', 'English', 85),
(6, 'Jyoti', 'Science', 70);


/*
    Subqueries were used to extract unique studentname and subjectname, and a cross join was performed to generate all possible combinations. 
    A left join between the cross join table and the main table will produce null if join condition is not met.

*/

SELECT 
    s1.studentname,
    s2.subjectname,
    s3.marks
FROM 
    (SELECT DISTINCT studentname FROM students_results) s1
CROSS JOIN 
    (SELECT DISTINCT subjectname FROM students_results) s2
LEFT JOIN 
    students_results s3
ON 
    s1.studentname = s3.studentname 
    AND s2.subjectname = s3.subjectname;


/* 

    Developed above solution using CTE's

*/


WITH Students AS (
    SELECT DISTINCT studentname
    FROM students_results
),
Subjects AS (
    SELECT DISTINCT subjectname
    FROM students_results
)
SELECT 
    s1.studentname,
    s2.subjectname,
    s3.marks
FROM 
    Students s1
CROSS JOIN 
    Subjects s2
LEFT JOIN 
    students_results s3
ON 
    s1.studentname = s3.studentname 
    AND s2.subjectname = s3.subjectname;


---------------------------------------------------------------------------------------------------------------------------------------
-- Question3
---------------------------------------------------------------------------------------------------------------------------------------

-- Creating tables

CREATE TABLE Customers (
    CustomerID VARCHAR(10) PRIMARY KEY,
    CompanyName VARCHAR(100),
    ContactName VARCHAR(100),
    ContactTitle VARCHAR(100),
    Address VARCHAR(200),
    City VARCHAR(100)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID VARCHAR(10),
    EmployeeID INT,
    OrderDate DATETIME,
    ShipVia INT,
    Freight DECIMAL(10, 2),
    ShipName VARCHAR(100),
    ShipAddress VARCHAR(200),
    ShipCity VARCHAR(100),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Inserting records 

/* 

    To maintain referential integrity, I have used available candidate Id's in customers table to insert into Orders table,
    not used records exactly given in the question. 

*/

INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City) VALUES
('AROUT', 'Around the Horn', 'Thomas Hardy', 'Sales Representative', '120 Hanover Sq.', 'London'),
('BERGS', 'Berglunds snabbköp', 'Christina Berglund', 'Order Administrator', 'Berguvsvägen  8', 'Luleå'),
('BLAUS', 'Blauer See Delikatessen', 'Hanna Moos', 'Sales Representative', 'Forsterstr. 57', 'Mannheim'),
('BLONP', 'Blondesddsl père et fils', 'Frédérique Citeaux', 'Marketing Manager', '24, place Kléber', 'Strasbourg'),
('BOLID', 'Bólido Comidas preparadas', 'Martín Sommer', 'Owner', 'C/ Araquil, 67', 'Madrid'),
('BONAP', 'Bon app''', 'Laurence Lebihan', 'Owner', '12, rue des Bouchers', 'Marseille'),
('BOTT', 'Bottom-Dollar Markets', 'Elizabeth Lincoln', 'Accounting Manager', '23 Tsawwassen Blvd.', 'Tsawwassen'),
('BSBEV', 'B''s Beverages', 'Victoria Ashworth', 'Sales Representative', 'Fauntleroy Circus', 'London'),
('CACTU', 'Cactus Comidas para llevar', 'Patricio Simpson', 'Sales Agent', 'Cerrito 333', 'Buenos Aires'),
('CENTC', 'Centro comercial Moctezuma', 'Francisco Chang', 'Marketing Manager', 'Sierras de Granada 9993', 'México D.F.'),
('CHOPS', 'Chop-suey Chinese', 'Yang Wang', 'Owner', 'Hauptstr. 29', 'Bern'),
('COMM', 'Comércio Mineiro', 'Pedro Afonso', 'Sales Associate', 'Av. dos Lusíadas, 23', 'São Paulo');

INSERT INTO Orders (OrderID, CustomerID, EmployeeID, OrderDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity) VALUES
(10643, 'AROUT', 6, '1997-08-25 00:00:00', 1, 29.46, 'Alfreds Futterkiste', 'Obere Str. 57', 'Berlin'),
(10692, 'AROUT', 4, '1997-10-03 00:00:00', 2, 61.02, 'Alfreds Futterkiste', 'Obere Str. 57', 'Berlin'),
(10702, 'AROUT', 4, '1997-10-13 00:00:00', 1, 23.94, 'Alfreds Futterkiste', 'Obere Str. 57', 'Berlin'),
(10835, 'AROUT', 1, '1998-01-15 00:00:00', 3, 69.53, 'Alfreds Futterkiste', 'Obere Str. 57', 'Berlin'),
(10952, 'AROUT', 3, '1998-03-16 00:00:00', 1, 40.42, 'Alfreds Futterkiste', 'Obere Str. 57', 'Berlin'),
(11011, 'AROUT', 6, '1998-04-09 00:00:00', 1, 1.21, 'Alfreds Futterkiste', 'Obere Str. 57', 'Berlin'),
(10926, 'BERGS', 4, '1998-03-04 00:00:00', 3, 39.92, 'Ana Trujillo Emparedados y helados', 'Avda. de la Constitución 2222', 'México D.F.'),
(10759, 'BERGS', 3, '1997-11-28 00:00:00', 1, 11.99, 'Ana Trujillo Emparedados y helados', 'Avda. de la Constitución 2222', 'México D.F.'),
(10625, 'BERGS', 3, '1997-08-08 00:00:00', 1, 43.90, 'Ana Trujillo Emparedados y helados', 'Avda. de la Constitución 2222', 'México D.F.'),
(10308, 'BERGS', 7, '1996-09-18 00:00:00', 1, 1.61, 'Ana Trujillo Emparedados y helados', 'Avda. de la Constitución 2222', 'México D.F.'),
(10365, 'BLAUS', 7, '1996-11-27 00:00:00', 2, 22.00, 'Antonio Moreno Taquería', 'Mataderos  2312', 'México D.F.');


/*

I have used windows function to solve this, Created CTE within that i have partioned the table based on customer ID's and order them in descending order
and assigned row numbers to each parttion. Finally selected all the required coulumns where rownumber is equal to 1.

*/

WITH LatestOrders AS (
    SELECT 
        CustomerID, 
        OrderID, 
        EmployeeID, 
        OrderDate, 
        ShipVia, 
        Freight, 
        ShipName, 
        ShipAddress, 
        ShipCity,
        ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY OrderDate DESC) AS RowNum
    FROM 
        Orders
)
SELECT 
    c.CustomerID,
    c.CompanyName,
    c.ContactName,
    c.ContactTitle,
    c.Address,
    c.City,
    lo.OrderID,
    lo.EmployeeID,
    lo.OrderDate,
    lo.ShipVia,
    lo.Freight,
    lo.ShipName,
    lo.ShipAddress
FROM 
    Customers c
LEFT JOIN 
    LatestOrders lo
ON 
    c.CustomerID = lo.CustomerID
WHERE 
    lo.RowNum = 1;

---------------------------------------------------------------------------------------------------------------------------------------
-- Question4
---------------------------------------------------------------------------------------------------------------------------------------

-- Developed the Recursive CTE table with all the values from 1 to n where n = 20


SET @num = 20;  -- this works in mysql server

WITH RECURSIVE Numbers AS (
    SELECT 1 AS number 
    UNION ALL
    SELECT number + 1
    FROM Numbers
    WHERE number < @num  
)
SELECT number
FROM Numbers;


---------------------------------------------------------------------------------------------------------------------------------------
-- Question5
---------------------------------------------------------------------------------------------------------------------------------------


-- Creating a table 

CREATE TABLE HierarchicalTable (
    Id INT PRIMARY KEY,
    EmpID INT NOT NULL,
    ParentID INT NOT NULL,
    Description VARCHAR(255) NOT NULL
);

-- inserting record into table 

INSERT INTO HierarchicalTable (Id, EmpID, ParentID, Description) VALUES
(1, 1, 0, 'Main Parent Yogi'),
(2, 2, 0, 'Main Parent Ron'),
(3, 3, 0, 'Main Parent Don'),
(4, 4, 2, 'Child Jaz'),
(5, 5, 2, 'Child Rat'),
(6, 6, 1, 'Child Tom'),
(7, 7, 2, 'Child Jerry'),
(8, 8, 3, 'Child Din'),
(9, 9, 1, 'Child Minny'),
(10, 10, 3, 'Child Micky'),
(11, 11, 3, 'Child Goofy'),
(12, 12, 3, 'Child Daisy'),
(13, 13, 6, 'Sub Child Popey'),
(14, 14, 6, 'Sub Child Zen'),
(15, 15, 9, 'Sub Child Shin Chan'),
(16, 16, 10, 'Sub Child Doremon'),
(17, 17, 9, 'Sub Child Pikachu'),
(18, 18, 8, 'Sub Child Tweety');

/*

started by designating root nodes with ParentID = 0 as Level 1 and using their description as the first breadcrumb. 
The level was then raised by 1 and the description of the current node was added to the breadcrumb trail 
using a recursive query to find all child nodes.

*/


WITH RECURSIVE Hierarchy AS (
    SELECT 
        Id,
        EmpID,
        ParentID,
        Description,
        1 AS Level, 
        CAST(Description AS CHAR(255)) AS Breadcrumb 
    FROM 
        HierarchicalTable
    WHERE 
        ParentID = 0

    UNION ALL

    SELECT 
        h.Id,
        h.EmpID,
        h.ParentID,
        h.Description,
        p.Level + 1 AS Level, 
        CONCAT(p.Breadcrumb, ' > ', h.Description) AS Breadcrumb 
    FROM 
        HierarchicalTable h
    INNER JOIN 
        Hierarchy p
    ON 
        h.ParentID = p.EmpID
)
SELECT 
    Id,
    EmpID,
    ParentID,
    Description,
    Level,
    Breadcrumb
FROM 
    Hierarchy;
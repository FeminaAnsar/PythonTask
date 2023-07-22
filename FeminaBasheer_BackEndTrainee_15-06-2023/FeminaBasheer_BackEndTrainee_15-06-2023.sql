show tables;
select * from customermaster_1220316839;
select * from salesorder_1220316839;
desc customermaster_1220316839;
desc salesorder_1220316839;
DESC CUSTOMER_SALES;
USE BEINEXSQL;
SELECT * FROM CUSTOMER_SALES;
/* Left Join */
CREATE TABLE CUSTOMER_SALES AS
(SELECT salesorder_1220316839.*, 
customermaster_1220316839.Customer, 
customermaster_1220316839.Region FROM salesorder_1220316839
LEFT JOIN customermaster_1220316839 ON 
salesorder_1220316839.Customer_ID = customermaster_1220316839.Customer_ID);

/*2) Write a command to display first 10 rows.*/
SELECT * FROM CUSTOMER_SALES LIMIT 10;

/*3)Identify unique items?*/
SELECT DISTINCT Item FROM CUSTOMER_SALES;

/*4)Identify any unit cost is negative?*/
SELECT * FROM CUSTOMER_SALES WHERE SIGN(UnitCost)=-1;

/*5) Identify minimum and maximum unit price happened for same item.*/
SELECT Item,MIN(UnitCost) AS MIN_PRICE,MAX(UnitCost) 
AS MAX_PRICE FROM CUSTOMER_SALES GROUP BY Item;

/*6)Identify the Total sales happened in the year of 2021?*/
SELECT SUM(Total) AS Total_Sales_2021 FROM CUSTOMER_SALES 
WHERE SUBSTRING(OrderDate,7)='2021';

/*7)Which item is sold maximum in the year 2021?*/
SELECT Item,sum(Total) FROM CUSTOMER_SALES  WHERE 
SUBSTRING(OrderDate,7)='2021' GROUP BY Item ORDER BY sum(Total) DESC LIMIT 1;

/*8)Identify the region with highest and lowest sales.*/
SELECT Region,MAX(Total) AS MAX_SALES FROM CUSTOMER_SALES GROUP BY Region 
ORDER BY MAX_SALES DESC LIMIT 1;
SELECT Region,MIN(Total) AS MIN_SALES FROM CUSTOMER_SALES GROUP BY Region 
ORDER BY MIN_SALES LIMIT 1;

/*9)Identify the customer name having highest sales for the year 2022.*/
SELECT Customer , MAX(Total) AS Highest_Sales
FROM CUSTOMER_SALES   WHERE SUBSTRING(OrderDate,7)='2022'
GROUP BY Customer
ORDER BY MAX(Total) DESC LIMIT 1;

/*10) Which item has highest and lowest unit cost?*/
SELECT Item,MAX(UnitCost) AS HighCost FROM CUSTOMER_SALES GROUP BY Item
ORDER BY HighCost DESC LIMIT 1;
SELECT Region,MIN(UnitCost) AS LowCost FROM CUSTOMER_SALES GROUP BY Item 
ORDER BY LowCost LIMIT 1;

/*11)Identify items starts with letter 'P'*/
SELECT DISTINCT Item FROM CUSTOMER_SALES WHERE Item LIKE 'p%' ;

/*12)Filter the table having items Pen and Pencil.*/
SELECT * FROM CUSTOMER_SALES WHERE Item='Pen' or Item='Pencil';

/*13)Filter the table with unit cost between 1 and 100.*/
SELECT * FROM CUSTOMER_SALES WHERE UnitCost BETWEEN 1 AND 100;

/*14) Identify the customer with more no of transaction(no of entries).*/
SELECT Customer,COUNT(*) AS NO_OF_TRANSACTIONS FROM CUSTOMER_SALES 
GROUP BY Customer ORDER BY NO_OF_TRANSACTIONS DESC LIMIT 1;

/*15) Identify which item has maximum sales in each region*/
SELECT Region,MAX(Item) AS Item,MAX(Total) AS MAX_SALES FROM 
CUSTOMER_SALES GROUP BY Region;

/*Create 5 more scenarios using important inbuilt functions of MySQL.*/
/*1) Find the total cost of all products*/
SELECT SUM(Total) AS TOTAL FROM CUSTOMER_SALES;

/*2)Find the maximum number of units */
SELECT MAX(Units) AS MAX_UNITS FROM CUSTOMER_SALES;

/*3) Round the Total where customer Id=c6*/
SELECT Customer_ID,Item,Round(Total) FROM CUSTOMER_SALES WHERE Customer_ID='C6';

/*4)Names of customers starting with J*/
SELECT Customer_ID,Customer FROM CUSTOMER_SALES WHERE Customer LIKE 'j%';

/*5)Names of customers starting with %e%*/
SELECT Customer_ID,Customer FROM CUSTOMER_SALES WHERE Customer LIKE '%e%';



 

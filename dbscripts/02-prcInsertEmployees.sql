CREATE Procedure prcInsertEmployees
(@json VARCHAR(MAX) = '')
AS
BEGIN


INSERT INTO tblEmployee 
SELECT name, city, department, gender
	FROM OPENJSON(@json)
	WITH (
		name NVARCHAR(50) '$.name',
		city NVARCHAR(50) '$.city',
		department NVARCHAR(50) '$.department',
		gender VARCHAR(1) '$.gender'
		)


--select * from tblemployee
--truncate table tblemployee


--INSERT INTO tblEmployee VALUES
--('Rahul','Bangalore','Cricket','M')

END

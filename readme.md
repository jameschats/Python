Topic - Python: Read JSON data and insert into SQL using PYODBC

Agenda
-------
python - how to make sql connection using pyodbc
call sql procedure to insert records to database (without parameters)
read json object and pass json to sql procedure
read json from json file and pass json to sql procedure
how to pass unicode (chinese, hindi) characters from json to sql




# read json data from file
with open("employee.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

# initialise json object
# data = [{"name": "sarath","city":"chennai","department":"software","gender":"m"}, 
# {"name": "rani","city":"pune","department":"banking","gender":"f"},
# {"name": "威明","city":"delhi","department":"economy","gender":"f"},
# {"name": "पांचाल","city":"hyderabad","department":"marketing","gender":"m"}
# ]

# convert json object to string
    json_string = json.dumps(data) 
	
	#, ensure_ascii=False)




[{"name": "sarath","city":"chennai","department":"software","gender":"m"}, 
{"name": "rani","city":"pune","department":"banking","gender":"f"},
{"name": "mary","city":"delhi","department":"economy","gender":"f"},
{"name": "rahul","city":"hyderabad","department":"marketing","gender":"m"},
{"name": "suresh","city":"kolkata","department":"digital marketing","gender":"m"}
]


[{"name": "sarath","city":"chennai","department":"software","gender":"m"}, 
{"name": "rani","city":"pune","department":"banking","gender":"f"},
{"name": "威明","city":"delhi","department":"economy","gender":"f"},
{"name": "पांचाल","city":"hyderabad","department":"marketing","gender":"m"},
{"name": "suresh","city":"kolkata","department":"digital marketing","gender":"m"}
]






ALTER Procedure prcInsertEmployees
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

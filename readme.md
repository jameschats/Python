Topic - Python: Read JSON data and insert into SQL using PYODBC

Agenda
-------
* python - how to make sql connection using pyodbc
* call sql procedure to insert records to database (without parameters)
* read json object and pass json to sql procedure
* read json from json file and pass json to sql procedure
* how to pass unicode (chinese, hindi) characters from json to sql




// read json data from file

with open("employee.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

// initialise json object

data = [{"name": "sarath","city":"chennai","department":"software","gender":"m"}, 
  {"name": "rani","city":"pune","department":"banking","gender":"f"},
  {"name": "威明","city":"delhi","department":"economy","gender":"f"},
  {"name": "पांचाल","city":"hyderabad","department":"marketing","gender":"m"}
 ]

convert json object to string
    json_string = json.dumps(data) 


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







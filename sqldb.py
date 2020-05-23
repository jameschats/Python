import pyodbc
import json

conn = pyodbc.connect('Driver={SQL Server};Server=.\SQLEXPRESS;Database=Employee;Trusted_Connection=yes;')
conn.timeout = 60    
conn.autocommit = True


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
        


    # Call SP and trap Error if raised
    try:        
        cursor = conn.cursor()
        # call sql server procedure with one parameter
        # cursor.execute('EXEC prcInsertEmployees')
        cursor.execute('EXEC prcInsertEmployees @json = ?', json_string)
        print('inserted data')    

    except pyodbc.Error as err:
        print('Error !!!!! %s' % err)
    except:
        print('something else failed miserably')

    conn.close()
    print('closed db connection')



















# https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15



# data = [{'name': 'sarath','city':'chennai','department':'software','gender':'m'}, 
# {'name': 'rani','city':'pune','department':'banking','gender':'f'},
# {'name': 'megha','city':'delhi','department':'economy','gender':'f'},
# {'name': 'abdul','city':'hyderabad','department':'marketing','gender':'m'}
# ]
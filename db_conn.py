import pyodbc

host = "DATACENTER"
database = "FLASK"
username = "bmoretz"
password = "l3tm31n"

print ("DB CONNECT ATTEMPT")
try:
    cnxn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=DATACENTER;Database=FLASK;UID=bmoretz;PWD=l3tm31n')
    print ("SUCCESS")
except Exception as e:
    print("Error: " + str(e))
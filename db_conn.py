import pyodbc

host = "DATACENTER"
database = "FLASK"
username = "bmoretz"
password = "l3tm31n"

print ("DB CONNECT ATTEMPT")
try:
    cs = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (host, username, password, database)
    cnxn = pyodbc.connect(cs)
    print ("SUCCESS")
except Exception as e:
    print ("Error: " + str(e))

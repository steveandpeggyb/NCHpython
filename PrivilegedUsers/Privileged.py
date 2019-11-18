import pyodbc
PASSWORD = 'RQ*50XR!'


cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=RDW-BCRSQL01;"
                      "Database=qpulse5;"
                      "uid=BCRReporting;"
                      "password=PASSWORD;")


cursor = cnxn.cursor()
cursor.execute('SELECT TOP 10 * from Person')

for row in cursor:
    print('row = %r' % (row,))
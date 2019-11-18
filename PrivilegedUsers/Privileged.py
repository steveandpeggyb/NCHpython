import pyodbc
PASSWORD = 'Gr1mjd#12'


# cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
#                       "Server=RDW-BCRSQL01;"
#                       "Database=qpulse5;"
#                       "uid=QPulseAppUser;"
#                       "password=PASSWORD;")
cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=RDW-BCRSQL01;DATABASE=qpulse5;UID=QPulseAppUser;PWD=PASSWORD", autocommit=True)

cursor = cnxn.cursor()
cursor.execute('SELECT TOP 10 * from Person')

for row in cursor:
    print('row = %r' % (row,))
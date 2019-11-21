import pyodbc as sql
# Create connection
SERVERNAME = 'RDW-BCRSQL01'
DATA_BASE_INFO = 'Qpulse5'
USERNAME = 'QPulseAppUser'
PASSWORD = 'Gr1mjd#12'












print("\r\n")

con = sql.connect(driver="{ODBC Driver 17 for SQL Server}",server=SERVERNAME,database=DATA_BASE_INFO,uid=USERNAME,password=PASSWORD, encoding='utf-8')
cur = con.cursor()
db_cmd = "SELECT TOP 10 FullName, JobTitle, ActiveDirectoryAlias FROM [QPulse5].[dbo].[Person] where IsDeleted = 0 AND IsUser = 1"
res = cur.execute(db_cmd)

# Do something with your result set, for example print out all the results:
if res == None:
    print("No data returned!")
else:
    for r in res:
        print(r)

print("\r\n")

# sql.close()


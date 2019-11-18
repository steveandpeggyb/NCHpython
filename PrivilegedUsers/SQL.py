import pyodbc as sql
# Create connection
SERVERNAME = '\\RSW-BCRSQL01'
DATA_BASE_INFO = 'Qpulse5'
USERNAME = 'bcrReporting'
PASSWORD = 'RQ*50XR!'
print("setup the connection.")











con = sql.connect(driver="{ODBC Driver 17 for SQL Server}",server=SERVERNAME,database=DATA_BASE_INFO,uid=USERNAME,password=PASSWORD, encoding='utf-8')
print("Line 20")
cur = con.cursor()
db_cmd = "SELECT TOP 10 FullName, JobTitle, ActiveDirectoryAlias FROM [QPulse5].[dbo].[Person] where IsDeleted = 0 AND IsUser = 1"
res = cur.execute(db_cmd)
# Do something with your result set, for example print out all the results:
for r in res:
    print(r)
sql.close()

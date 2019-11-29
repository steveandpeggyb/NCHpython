import pyodbc as sql
import os   

# Create connection
SERVERNAME = 'RDW-BCRSQL01'
DATA_BASE_INFO = 'Qpulse5'
USERNAME = os.environ.get('DB_USER_DEV_QP')
PASSWORD = os.environ.get('DB_PW_DEV_QP')

print("\r\n")
con = sql.connect(driver="{ODBC Driver 17 for SQL Server}",server=SERVERNAME,database=DATA_BASE_INFO,uid=USERNAME,password=PASSWORD, encoding='utf-8')
cur = con.cursor()
db_cmd = """
DROP TABLE IF EXISTS ##databaseperms

CREATE TABLE ##databaseperms
(
	  dbname varchar(50)
	, dbrolename varchar(50)
	, dbusernames varchar(max)
)

DECLARE @databaseid int, 
		@dbname varchar(50), 
		@useStatement nvarchar(100), 
		@insertStatement nvarchar(max)

SELECT @databaseID = MIN(database_id) 
FROM sys.databases
WHERE name NOT IN ('InfoRepo')

while @databaseid IS NOT NULL
BEGIN
       select @dbname = name FROM sys.databases WHERE database_id = @databaseid
       SELECT @useStatement = 'USE ' + @dbname
       EXEC sp_executesql @useStatement
       select @insertStatement = 
								   'USE ' + @dbName + '; INSERT INTO ##databaseperms
								   SELECT DB_NAME(), DP1.name AS DatabaseRoleName,   
									  BCR.dbo.ToListSorted(isnull (DP2.name, ''No members'')) AS DatabaseUserName   
									FROM sys.database_role_members AS DRM  
									RIGHT OUTER JOIN sys.database_principals AS DP1  
									  ON DRM.role_principal_id = DP1.principal_id  
									LEFT OUTER JOIN sys.database_principals AS DP2  
									  ON DRM.member_principal_id = DP2.principal_id  
								   WHERE DP1.type = ''R'' and dp1.name IN (''db_owner'', ''db_datawriter'')
								   GROUP BY DP1.name
								   ORDER BY DP1.name;  '
       EXEC sp_executeSQL  @insertStatement
       SELECT @databaseid = MIN(database_id) from sys.databases WHERE database_id > @databaseid and name NOT IN ('InfoRepo')
END

select
	dbusernames
FROM ##databaseperms

union

--SELECT   name,type_desc,is_disabled
select name as dbusernames
FROM     master.sys.server_principals 
WHERE    IS_SRVROLEMEMBER ('sysadmin',name) = 1
"""

try:
    res = cur.execute(db_cmd)

    # Do something with your result set, for example print out all the results:
    if res == None:
        print("No data returned!")
    else:
        for r in res:
            print(r[2], '\t', r[0])

    print("\r\n")

except Exception as e:
    print("ERROR",e)

else:
    print("No Errors")

finally:
    print("Now closing the 'SQL.py' module.")

con.close()


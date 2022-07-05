#need to download pyodbc library 
#need to install the ODBC Driver 13 for SQL Server driver 

import pyodbc 
server = 'emprodprogtool.database.windows.net' 
database = 'em_onlinedb_db' 
username = 'eitanmedicalsa' 
password = 'Sighsu2007' 
driver= '{ODBC Driver 13 for SQL Server}'

query= "SELECT * FROM VersionInfos"

try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    print('Connection established')
    cursor.execute(query)
    allrows = cursor.fetchall()
    for row in allrows:
        print(f'row = {row}')
        print()
        
except:
     print('Cannot connect to SQL server')
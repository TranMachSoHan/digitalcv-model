import pymysql
import pandas
# Database parameter
host = 'hc0vm00007.apac.bosch.com'
user = 'digitalcv-dev'      
passwd = 'tXS0CZSI+x3FLz4SG'
database = 'digitalcv-dev'

try:
    # Connect to the database
    connection = pymysql.connect(host='hc0vm00007.apac.bosch.com',
                             user='digitalcv-dev',
                             password='tXS0CZSI+x3FLz4SG',
                             db='digitalcv-dev')
    
    cursor=connection.cursor()
    cursor.execute("SELECT id, name, url FROM courses")  
    row = cursor.fetchall()  
    df = pandas.DataFrame(row, columns=['id', 'name', 'url'])
    print(df)
    print('Type of courses ', type(df))
except :
    print("error")

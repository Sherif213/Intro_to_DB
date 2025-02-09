import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost"
        user = "root"
        password = "1532910"
        database = "alx_africa"
    )
    
    
except:
    print("DataBase connection failed")
    
cur = mydb.cursor
try: 
    cur.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except:
    print("Error")
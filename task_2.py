import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1532910",
        database = "alx_africa",
    )
    

except mysql.connector.Error as err:
    print("DataBase connection failed")
    
cur = mydb.cursor
try: 
    cur.execute("""CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    price float,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ,

);""")
    
except:
    print("Error")

try: 
    cur.execute("""CREATE TABLE Authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215) 
);""")
    
except:
    print("Error")
    
try: 
    cur.execute("""CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);""")
    
except:
    print("Error")
    
try: 
    cur.execute("""CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    order_date DATE,
);""")
    
except:
    print("Error")

try: 
    cur.execute("""CREATE TABLE Order_Details(

    quantity DOUBLE, 
    FOREIGN KEY (order_id) REFERENCES Orders(order_id), 
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
);""")
    
except:
    print("Error")
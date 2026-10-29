
import mysql.connector
from getpass import getpass

password = getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=password,
    database="banking_analytics"
)

print("Connected to the database!")

connection.close()
print("Database connection closed.")

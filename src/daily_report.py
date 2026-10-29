
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

print("Connected to MySQL successfully!")
cursor=connection.cursor()
cursor.execute("select* from transactions")

rows = cursor.fetchall()

columns = [column[0] for column in cursor.description]
print(columns)

for row in rows:
    print(row)

cursor.execute(
    "SELECT SUM(amount) FROM transactions"
)

total_amount = cursor.fetchone()[0]

print("Total transaction amount:", total_amount)


cursor.close()
connection.close()
print("Database connection closed.")




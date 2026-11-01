
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
# Count total transactions
cursor.execute("SELECT COUNT(*) FROM transactions")
total_transactions = cursor.fetchone()[0]

# Count successful transactions
cursor.execute(
    "SELECT COUNT(*) FROM transactions WHERE status = 'SUCCESS'"
)
successful_transactions = cursor.fetchone()[0]

# Count failed transactions
cursor.execute(
    "SELECT COUNT(*) FROM transactions WHERE status = 'FAILED'"
)
failed_transactions = cursor.fetchone()[0]

print("Total transactions:", total_transactions)
print("Successful transactions:", successful_transactions)
print("Failed transactions:", failed_transactions)

# Transaction analysis by type
cursor.execute("""
    SELECT
        transaction_type,
        COUNT(*) AS total_transactions,
        SUM(amount) AS total_amount
    FROM transactions
    GROUP BY transaction_type
""")

results = cursor.fetchall()

print("\nTransaction Analysis:")

for row in results:
    print(row)

cursor.close()
connection.close()
print("Database connection closed.")





import pandas as pd
import mysql.connector
from getpass import getpass

# Step 1: Read the cleaned CSV file
df = pd.read_csv("data/processed/valid_transactions.csv")

print("CSV file loaded successfully!")
print("Total records:", len(df))

# Step 2: Connect to MySQL
password = getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=password,
    database="banking_analytics"
)

cursor = connection.cursor()


# Step 3: Insert records into MySQL
query = """
INSERT IGNORE INTO transactions
(transaction_id, customer_id, transaction_type, amount, transaction_date, status)
VALUES (%s, %s, %s, %s, %s, %s)
"""

inserted_count = 0

for _, row in df.iterrows():
    cursor.execute(query, tuple(row))
    inserted_count += cursor.rowcount

# Step 4: Save changes
connection.commit()

print("Records inserted successfully:", inserted_count)

# Step 5: Close the connection
cursor.close()
connection.close()

print("Database connection closed.")



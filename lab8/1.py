#    1.	Write a Python Program to perform the following tasks:
#       a.	Create a database ‘student.db’ and connect to that database
#       b.	Create a function addTable() that will add new table with columns like 
#           (S.No accepting numeric values and Primary Key, SName accepting String values and NOT NULL, 
#           Contact No accepting numeric values) to the Database
#       c.	Create a function addRecords() to add the records to table (Values to insert to be taken from the user)
#       d.	Function ViewRecords() to view the records from the table.
#       e.	Function UpdateRecord() to update the record of a table

import sqlite3

def connect_db():
    return sqlite3.connect("lab8.db")

def addTable():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lab8(
            SNo INTEGER PRIMARY KEY,
            SName TEXT NOT NULL,
            ContactNo INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'lab8' created successfully.")

# c. Create a function addRecords() to add records to the table
def addRecords():
    conn = connect_db()
    cursor = conn.cursor()
    SNo = int(input("Enter S.No: "))
    SName = input("Enter Student Name: ")
    ContactNo = int(input("Enter Contact No: "))

    cursor.execute('''
        INSERT INTO lab8 (SNo, SName, ContactNo)
        VALUES (?, ?, ?)
    ''', (SNo, SName, ContactNo))

    conn.commit()
    conn.close()
    print("Record added successfully.")

# d. Create a function ViewRecords() to view records from the table
def ViewRecords():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lab8")
    records = cursor.fetchall()
    for record in records:
        print("S.No:", record[0], " | Name:", record[1], " | Contact No:", record[2])
    conn.close()

# e. Create a function UpdateRecord() to update a record in the table
def UpdateRecord():
    conn = connect_db()
    cursor = conn.cursor()
    SNo = int(input("Enter the S.No of the student you want to update: "))
    new_name = input("Enter the new name: ")
    new_contact = int(input("Enter the new contact number: "))

    cursor.execute('''
        UPDATE lab8
        SET SName = ?, ContactNo = ?
        WHERE SNo = ?
    ''', (new_name, new_contact, SNo))

    conn.commit()
    conn.close()
    print("Record updated successfully.")

# Main program to call functions
def main():
    addTable()
    while True:
        print("\nChoose an option:")
        print("1. Add a new record")
        print("2. View records")
        print("3. Update a record")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            addRecords()
        elif choice == '2':
            ViewRecords()
        elif choice == '3':
            UpdateRecord()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()
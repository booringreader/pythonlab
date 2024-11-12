# WAP to count total number of records in a table created in Program 1

import sqlite3

def record_count():
    try:
        DBconnect = sqlite3.connect('lab8.db')
        cursor = DBconnect.cursor()
    
        cursor.execute("SELECT COUNT(*) FROM lab8")

        tables = cursor.fetchone()[0]

        print(f"Total number of records in the table: {tables}")
    
    except sqlite3.Error as e:
        print("An error occurred:", e)
    
    finally:
        # Close the database connection
        if DBconnect:
            DBconnect.close()

record_count()

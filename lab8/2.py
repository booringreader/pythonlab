# WAP to find list out all the tables in a database

import sqlite3

def tablesLIS(DB_NAME):
    try:
        DBconnect = sqlite3.connect(DB_NAME)
        cursor = DBconnect.cursor()
        
        # list tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        
        # Fetch all table names
        tables = cursor.fetchall()
        
        # Check if there are any tables in the database
        if tables:
            print(f"Tables in the database '{DB_NAME}':")
            for table in tables:
                print(table[0]) 
        else:
            print(f"No tables found in the database '{DB_NAME}'.")
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        
    finally:
        if DBconnect:
            DBconnect.close()

# Example usage
tablesLIS('lab8.db')

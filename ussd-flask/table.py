
import sqlite3

# create a database connection
conn = sqlite3.connect('ussd.db')
# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE membership (
            name text,      
            phone_number text
            )""")
# commit our command
conn.commit()
# close our connection
conn.close()

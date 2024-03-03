import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('games.db')  # Ensure this matches the database name
cur = conn.cursor()

# Drop the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS games')  # Change 'deployments' to 'games'
print("Table dropped successfully")

# Create the table again with appropriate column names for game data
conn.execute('CREATE TABLE games (Rank INTEGER, Name TEXT, Year INTEGER, Genre TEXT, Publisher TEXT, Global_Sales TEXT)')
print("Table created successfully")

# Open the file to read it into the database
with open('games/game.csv', newline='') as f:  # Ensure the path matches where your CSV file is located
    reader = csv.reader(f, delimiter=",")
    next(reader, None)  # Skip the header row
    for row in reader:
        # Insert data into the 'games' table
        cur.execute('INSERT INTO games VALUES (?, ?, ?, ?, ?, ?)', 
                    (row[0], row[1], row[2], row[3], row[4], row[10]))  # Make sure these indices match your CSV structure
        conn.commit()
print("Data parsed successfully")

conn.close()

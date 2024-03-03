from flask import Flask, render_template, request, redirect, url_for
import sqlite3  # Import sqlite3 module to interact with SQLite database.

app = Flask(__name__)

db_name = 'games.db'  # Define the name of the SQLite database file.

@app.route('/')       # Define the route for the home page.
def index():
  return render_template('index.html')   # Serve the index.html template for the home page.

@app.route('/game_details', methods=['GET', 'POST']) # Define the route for the game details page, allowing both GET and POST requests.
def game_details():
  conn = sqlite3.connect(db_name)#Connect to the SQLite database.
  conn.row_factory = sqlite3.Row #Configure connection to return rows as dictionary-like objects.
  cur = conn.cursor()            #Create a object to interact with the database.
  if request.method == 'POST':   #Check if the current request is a POST request.
    search_query = request.form['search']# Get the search query from the form data.
    cur.execute("SELECT Rank, Name, Global_Sales FROM games WHERE Name LIKE ?", ('%' + search_query + '%',))# Execute a SQL query to find games matching the search query.
  else:
    cur.execute("SELECT Rank, Name, Global_Sales FROM games")# If not a POST request, select all games from the database.

  games = cur.fetchall()         #Get all search results
  conn.close()                   #Close the database connection.
  return render_template('game_details.html', games=games)#Restart the game_details.html page to pass on the results of the search just done

@app.route('/sales_details', methods=['GET', 'POST'])# Define the route for the sales details page, allowing both GET and POST requests.
def sales_details():
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()

  if request.method == 'POST':
    search_query = request.form['search']
    cur.execute("SELECT Name, Year, Publisher, Global_Sales FROM games WHERE Name LIKE ?", ('%' + search_query + '%',))
  else:
    cur.execute("SELECT Name, Year, Publisher, Global_Sales FROM games")

  sales_info = cur.fetchall()
  conn.close()
  return render_template('sales_details.html', sales_info=sales_info)


app.run(debug=True)

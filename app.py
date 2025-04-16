#!/usr/bin/env python3
"""
Flask Basketball Database Application
====================================

Author: Kevin Sandke
Course: CSCI 3308 - Software Development Methods and Tools
Date: April 15, 2025

This application demonstrates a simple Flask web application with PostgreSQL 
database integration. It provides basic CRUD operations on a basketball players 
database through various endpoints.

The application connects to a PostgreSQL database hosted on DigitalOcean's 
managed database service and provides endpoints for creating a table, 
inserting data, querying data, and dropping the table.
"""

import os
from flask import Flask
import psycopg2

# Initialize Flask application
app = Flask(__name__)

# Database connection string (using environment variable would be more secure)
DATABASE_URL = "postgresql://ksandkedb_user:xPBtNZmK5OvxkI09Zg1udUVlzQJWRshx@dpg-cvm7fmqdbo4c738st03g-a/ksandkedb"

@app.route('/')
def hello_world():
    """
    Root endpoint that displays a simple greeting message.
    
    Returns:
        str: A greeting message including the author's name and course number.
    """
    return 'Hello World from Kevin Sandke in 3308'

@app.route('/db_test')
def db_test():
    """
    Test the database connection.
    
    This endpoint attempts to establish a connection to the PostgreSQL database
    and returns a success message if the connection is established properly.
    
    Returns:
        str: A message indicating the success of the database connection.
    """
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    # Close the connection immediately (just testing connection)
    conn.close()
    return "Database connection successful!"

@app.route('/db_create')
def db_create():
    """
    Create the Basketball table in the database.
    
    This endpoint creates a table named 'Basketball' with columns for player
    information if it doesn't already exist.
    
    Table Schema:
        - First: Player's first name (varchar)
        - Last: Player's last name (varchar)
        - City: City where the team is based (varchar)
        - Name: Team name (varchar)
        - Number: Player's jersey number (integer)
    
    Returns:
        str: A message indicating the table was created.
    """
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    # Create Basketball table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),  -- Player's first name
            Last varchar(255),   -- Player's last name
            City varchar(255),   -- City where the team is based
            Name varchar(255),   -- Team name
            Number int           -- Player's jersey number
        );
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    return "Basketball Table Created"

@app.route('/db_insert')
def db_insert():
    """
    Populate the Basketball table with sample data.
    
    This endpoint inserts five rows of basketball player data into the 
    Basketball table, including current NBA players and a custom entry
    for the application author.
    
    Returns:
        str: A message indicating the data was inserted.
    """
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    # Insert sample basketball player data
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Kevin', 'Sandke', 'CU Boulder', 'Buffs', 3308);
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    """
    Display all records from the Basketball table.
    
    This endpoint queries all records from the Basketball table and 
    formats the results as an HTML table for display in a web browser.
    
    Returns:
        str: HTML content displaying the data in a formatted table.
    """
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    # Query all records from the Basketball table
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    
    # Format data as an HTML table
    table_html = "<html><body><table border='1'>"
    # Add table headers
    table_html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    
    # Add rows with data
    for row in records:
        table_html += "<tr>"
        for col in row:
            table_html += f"<td>{col}</td>"
        table_html += "</tr>"
    
    table_html += "</table></body></html>"
    
    # Close connection
    conn.close()
    return table_html

@app.route('/db_drop')
def db_drop():
    """
    Drop the Basketball table from the database.
    
    This endpoint removes the Basketball table and all its data from
    the database. This is a destructive operation and should be used with caution.
    
    Returns:
        str: A message indicating the table was dropped.
    """
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    # Drop the Basketball table
    cur.execute("DROP TABLE Basketball;")
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"

if __name__ == '__main__':
    """
    Run the Flask application when the script is executed directly.
    
    This block configures the application to listen on all available network
    interfaces (0.0.0.0) on the port specified by the PORT environment variable
    or on port 10000 if the environment variable is not set.
    """
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

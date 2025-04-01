import os
from flask import Flask
import psycopg2

app = Flask(__name__)


DATABASE_URL = "postgresql://ksandkedb_user:xPBtNZmK5OvxkI09Zg1udUVlzQJWRshx@dpg-cvm7fmqdbo4c738st03g-a/ksandkedb"

@app.route('/')
def hello_world():
    return 'Hello World from Kevin Sandke in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect(DATABASE_URL)
    conn.close()
    return "Database connection successful!"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    
    conn.commit()
    conn.close()
    return "Basketball Table Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Kevin', 'Sandke', 'CU Boulder', 'Buffs', 3308);
    ''')
    
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
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
    
    conn.close()
    return table_html

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    cur.execute("DROP TABLE Basketball;")
    
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
# Flask Basketball Database Application

## Overview

This Flask application demonstrates a simple web application with PostgreSQL database integration for managing basketball player information. The application provides various endpoints to perform basic CRUD (Create, Read, Update, Delete) operations on a basketball players database.

## Author
Kevin Sandke  
CSCI 3308 - Software Development Methods and Tools  
University of Colorado Boulder

## Technologies Used
- **Python**: The core programming language for the application
- **Flask**: A lightweight web framework for Python
- **PostgreSQL**: A powerful, open-source relational database
- **psycopg2**: A PostgreSQL adapter for Python
- **HTML**: Used for formatting the data display

## Database Schema

The application uses a single table called `Basketball` with the following schema:

| Column | Type | Description |
|--------|------|-------------|
| First | varchar(255) | Player's first name |
| Last | varchar(255) | Player's last name |
| City | varchar(255) | City where the team is based |
| Name | varchar(255) | Team name |
| Number | int | Player's jersey number |

## Endpoints

The application provides the following endpoints:

### 1. Root Endpoint (`/`)
Displays a simple greeting message showing the author's name and course number.

### 2. Database Test (`/db_test`)
Tests the connection to the PostgreSQL database and returns a success message if the connection is established successfully.

### 3. Create Table (`/db_create`)
Creates the `Basketball` table in the database if it doesn't already exist.

### 4. Insert Data (`/db_insert`)
Populates the `Basketball` table with sample data of NBA players and a custom entry for the application author.

### 5. Display Data (`/db_select`)
Queries all records from the `Basketball` table and displays them in an HTML-formatted table.

### 6. Drop Table (`/db_drop`)
Removes the `Basketball` table from the database (destructive operation).

## External Files and Dependencies

### External Libraries
- **Flask**: Web framework installed via pip
- **psycopg2**: PostgreSQL adapter installed via pip

### External Resources
- **PostgreSQL Database**: The application connects to a PostgreSQL database hosted on DigitalOcean's managed database service.
- **No templates are used**: This application uses simple string responses and basic HTML formatting for the `/db_select` endpoint rather than template files.

## Setup and Deployment

### Local Development
1. Install the required dependencies:
   ```
   pip install flask psycopg2
   ```

2. Configure the database connection:
   The application uses a hardcoded connection string in the code. For better security in a production environment, this should be moved to an environment variable.

3. Run the application:
   ```
   python app.py
   ```
   The application will be available at http://localhost:10000

### Deployment
The application is designed to be deployable to platforms like Heroku by:
- Using the PORT environment variable if available
- Binding to all network interfaces (0.0.0.0)

## Usage Flow

A typical usage flow for this application would be:

1. Visit `/db_test` to verify database connection
2. Visit `/db_create` to create the table
3. Visit `/db_insert` to populate the table with sample data
4. Visit `/db_select` to view the data
5. Visit `/db_drop` to remove the table when finished

## Security Considerations

This application is a simple demonstration and has several security considerations that should be addressed for production use:

- The database credentials are hardcoded in the application code
- There is no input validation or sanitization
- No authentication or authorization mechanisms are implemented
- No error handling for database operations

## Future Improvements

Potential improvements to this application include:

- Moving database credentials to environment variables
- Adding proper error handling for database operations
- Implementing a form-based interface for data entry
- Adding update and delete operations for individual records
- Implementing user authentication
- Using template files for more sophisticated HTML rendering

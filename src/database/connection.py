import psycopg2

# Sets the information about the db
database_info = {
    'database': 'exempledb',
    'user': 'docker',
    'password': 'docker',
    'host': '0.0.0.0',
}

# Create the connectio with the db
def connect():
    database = psycopg2.connect(**database_info)
    return database

try:
    database = connect()
    print("Connection successful!")

except Exception as e:
    print(f"Error connecting to database: {e}")
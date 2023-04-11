import psycopg2

# Sets the information about the db
database_info = {
    "host":"localhost",
    "port":5432,
    "dbname":"exampledb",
    "user":"docker",
    "password":"docker"
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
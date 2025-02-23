import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_DATABASE = os.getenv('DATABASE')
DB_USERNAME = os.getenv('NAME')
DB_HOSTNAME = os.getenv('HOSTNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_PORT = os.getenv('PORT')

connection = psycopg2.connect(database = DB_DATABASE, 
                              user = DB_USERNAME,
                              password = DB_PASSWORD,
                              host = DB_HOSTNAME,
                              port = DB_PORT)

cursor = connection.cursor()

def get_cursor():
    return cursor

def commit():
    return connection.commit()

def init_database():
    cursor.execute('''CREATE TABLE users 
               (id SERIAL PRIMARY KEY, 
                name VARCHAR(100) NOT NULL,
                goal VARCHAR(100) NOT NULL,
                level VARCHAR(100) NOT NULL,
                workout_type VARCHAR(100) NOT NULL)''')
    cursor.execute('''CREATE TABLE exercises
                   (id SERIAL,
                   name VARCHAR(200) NOT NULL,
                   muscle VARCHAR(50) NOT NULL,
                   type VARCHAR(50) NOT NULL,
                   plan VARCHAR(20) NOT NULL,
                   instructions VARCHAR NOT NULL,
                   user_id INTEGER NOT NULL,
                   PRIMARY KEY (id),
                   FOREIGN KEY (user_id) REFERENCES users(id))''')
    commit()
    
# init_database()
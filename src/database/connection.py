import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE = os.environ.get("POSTGRES_DATABASE")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")

def new_database_connection(auto_commit=True):
    connection = psycopg2.connect(database=DATABASE, host=HOST, port=PORT, user=USER, password=PASSWORD)
    connection.autocommit = auto_commit
    cursor = connection.cursor()
    return connection, cursor
from database.connection import new_database_connection

def create_pg_schema():
  connection, cursor = new_database_connection()

  cursor.execute("""                 
    CREATE TABLE IF NOT EXISTS questions (
      id integer PRIMARY KEY,
      question text   
    );
                 
    CREATE TABLE IF NOT EXISTS responses (
      id integer PRIMARY KEY,
      question_id integer REFERENCES questions(id) ON DELETE CASCADE,  
      response text
    );
  """)

  print("Tables created")
  connection.close()

if __name__ == "__main__":
  create_pg_schema()
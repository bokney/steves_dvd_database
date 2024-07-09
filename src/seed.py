from connection import connect_to_db, close_db_connection

def seed():
    try:
        db = connect_to_db()
        db.run( """
            DROP DATABASE IF EXISTS dvd_database;
            CREATE DATABASE dvd_database;
        """ )
        pass
    finally:
        pass

seed()
# import os
from dotenv import load_dotenv
import pg8000.native
from db.config import database, password, user


load_dotenv(override=True)


def connect_to_db():
    return pg8000.native.Connection(
        user=user,
        password=password,
        database=database,
        # host=os.getenv("PG_HOST"),
        # port=int(os.getenv("PG_PORT"))
    )


def close_db_connection(conn):
    conn.close()
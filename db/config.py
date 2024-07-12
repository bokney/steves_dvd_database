import os
from dotenv import load_dotenv

TESTING = os.environ.get("TESTING")

if TESTING:
    load_dotenv(".env.test")
else:
    load_dotenv(".env.dev")

database = os.environ.get("PG_DATABASE")
password = os.environ.get("PG_PASSWORD")
user = os.environ.get("PG_USER")
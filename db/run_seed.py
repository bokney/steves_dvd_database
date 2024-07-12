from db.seed import seed

def seed_db() -> None:
    try:
        seed()
    except Exception as e:
        print(e)
        raise e

seed_db()
from db.connection import connect_to_db, close_db_connection

def seed():
    print('opening db connection')
    db = connect_to_db()
    db.run("DROP TABLE IF EXISTS items;")
    db.run("""
        CREATE TABLE items(
            item_id SERIAL PRIMARY KEY,
            name VARCHAR(128) NOT NULL,
            description VARCHAR(512) NOT NULL,
            cast_members VARCHAR(128)
        );
    """)
    print('closing db connection')
    close_db_connection(db)

seed()

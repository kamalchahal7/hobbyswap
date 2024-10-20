import sqlite3


def create_or_init_sqlite_database(filename):
    """create a database connection to an SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(filename)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

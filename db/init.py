import sqlite3
import os

def create_or_init_sqlite_database(filename):
    """create a database connection to an SQLite database"""
    conn = None
    try:
        # check if the database file already exists 
        db_exists = os.path.exists(filename)

        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        
        if not db_exists:
            # Schema initialization: Create a users table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    email TEXT NOT NULL,
                    password_hash TEXT NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    date_of_birth DATETIME NOT NULL,
                );        
            ''')

            # Schema initialization: Create a comments table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    text TEXT NOT NULL,
                    owner INTEGER,
                    listing INTEGER,
                    reply_to INTEGER,
                    FOREIGN KEY (owner) REFERENCES users(id),
                    FOREIGN KEY (listing) REFERENCES listings(id),
                    FOREIGN KEY (reply_to) REFERENCES comments(id)
                );
            ''')

            # Schema initialization: Create a listings table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS listings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    title TEXT,
                    description TEXT,
                    condition TEXT,
                    date_posted DATETIME DEFAULT CURRENT_TIMESTAMP,
                    owner INTEGER,
                    looking_for TEXT,
                    FOREIGN KEY (owner) REFERENCES users(id),
                );      
            ''')

            # Schema initialization: Create a tags table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tags (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    value TEXT NOT NULL,
                );
            ''')

            # Schema initialization: Create a categories table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                );
            ''')

            # Junction Tables for Many to Many Relationships (listing & tags, listing & categories)

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS listing_tags (
                    listing_id INTEGER,
                    tag_id INTEGER,
                    FOREIGN KEY (listing_id) references listings(id),
                    FOREIGN KEY (tag_id) references tags(id)
                 );
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS listing_categories (
                    listing_id INTEGER,
                    category_id INTEGER,
                    FOREIGN KEY (listing_id) references listings(id),
                    FOREIGN KEY (category_id) references categories(id)
                );
            ''')

            # Commit the changes
            conn.commit()
            print("Schema initialized.")
        else:
            print(f"Database '{filename}' already exists. No initialization needed.")

    except sqlite3.Error as e:
        print(e)

    finally:
        if conn:
            conn.close()

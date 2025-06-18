import sqlite3

def init_db():
    conn = sqlite3.connect('store_results.db')
    cursor = conn.cursor()

    # Create classification table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classification (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT,
            features TEXT,
            predicted_label TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create regression table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS regression (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT,
            features TEXT,
            predicted_value REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database and tables created!")

if __name__ == "__main__":
    init_db()

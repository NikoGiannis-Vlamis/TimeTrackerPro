import sqlite3

def init_db():
    conn=sqlite3.connect('timetracker.db')
    cursor=conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            start_time TEXT,
            end_time TEXT,
            hourly_rate REAL,
            total_earnings REAL,
            job_title TEXT
        )
    """)

    conn.commit()
    conn.close()
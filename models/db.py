import sqlite3

DATABASE_NAME = "laundrify.db"

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "EMPLOYEES" (
        "EmpID" INTEGER,
        "FirstName" TEXT NOT NULL,
        "LastName"  TEXT NOT NULL,
        "Password"  TEXT NOT NULL,
        "Position"  TEXT NOT NULL,
        "DateCreated"   TEXT DEFAULT CURRENT_DATE,
        PRIMARY KEY("EmpID" AUTOINCREMENT)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "CUSTOMERS" (
        "CustomerID"    INTEGER,
        "FirstName" TEXT NOT NULL,
        "LastName"  TEXT NOT NULL,
        "ContactNumber" TEXT NOT NULL,
        "Address"   TEXT NOT NULL,
        "DateRegistered"    TEXT DEFAULT CURRENT_DATE,
        PRIMARY KEY("CustomerID" AUTOINCREMENT)
        )
    """)

    cursor.execute('SELECT * FROM "EMPLOYEES" WHERE "Position" = ?', ("Admin",))
    user = cursor.fetchone()

    if user is None:
        cursor.execute("""
            INSERT INTO "EMPLOYEES" ("FirstName", "LastName", "Password", "Position")
            VALUES (?, ?, ?, ?)
        """, ("System", "Admin", "admin123", "Admin"))
        
        cursor.execute("""
            INSERT INTO "EMPLOYEES" ("FirstName", "LastName", "Password", "Position")
            VALUES (?, ?, ?, ?)
        """, ("Arabella", "Andal", "staff123", "Staff"))

    conn.commit()
    conn.close()
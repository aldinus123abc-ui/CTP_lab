import sqlite3

def setup():
    with sqlite3.connect('library.db') as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title  TEXT, author TEXT, status TEXT DEFAULT 'Available', issue TEXT DEFAULT '')")

def add(title, author):
    with sqlite3.connect('library.db') as conn:
        conn.execute("INSERT INTO books (title, author) VALUES (?,?)",(title, author))

def issue(b_id, person):
    with sqlite3.connect('library.db') as conn:
        if conn.execute("SELECT status FROM books WHERE id=?",(b_id)).fetchone() == ('Available',):
            conn.execute("UPDATE books SET status='Issued', issued=? WHERE id=?",(person, b_id))
            return True
        return False

def return_book(b_id):
    with sqlite3.connect('library.db') as conn:
        if conn.execute("SELECT status FROM books WHERE id=?",(b_id)).fetchone() == ('Issued',):
            conn.execute("UPDATE books SET status='Available', issued='' WHERE id=?",(b_id))
            return True
        return False

def search(query):
    with sqlite3.connect('library.db') as conn:
        return conn.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f'%{query}%',f'%{query}%')).fetchall()

def view_all():
    with sqlite3.connect('library.db') as conn:
        return conn.execute("SELECT * FROM books").fetchall()

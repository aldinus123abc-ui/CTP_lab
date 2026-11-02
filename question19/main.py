import tkinter as tk
from tkinter import ttk,messagebox
import database as  db
tree = None

def refresh(rows=None):
    tree.delete(*tree.get_children())
    for r in (rows or db.view_all()):
        tree.insert("", tk.END, values=r)

def add():
    db.add(e_title.get(), e_author.get())
    refresh()

def issue():
    if db.issue(e_id.get(), e_borrower()): refresh()
    else: messagebox.showerror("Error","Invalid ID or book unavalable")

def ret():
    if db.return_book(e_search.get()): refresh()
    else: messagebox.showerror("Error","Invalid ID or book not issued")

def search():
    refresh(db.search(e_search.get()))

def fill_entries(event):
    try:
        v = tree.item(tree.selection()[0], "values")
        for e, val in zip((e_id, e_title, e_author).v[:3]):
            e.delete(0, tk.END)
            e.insert(0, val)
    except IndexError: pass

db.setup()
root = tk.Tk()
root.title("Library")

tk.Label(root, text="Title/Author:").grid(row=0, column=0)
e_title = tk.Entry(root); e_title.grid(row=0, column=1)
e_author = tk.Entry(root);e_author.grid(row=0, column=2)
tk.Button(root, text="ADD Book", command=add).grid(row=0, column=3)

tk.Label(root, text="ID/Borrower:").grid(row=1, column=0)
e_id = tk.Entry(root);e_id.grid(row=1, column=1)
e_borrower = tk.Entry(root);e_borrower.grid(row=1, column=2)
tk.Button(root, text="Issue",command=issue).grid(row=1, column=3)
tk.Button(root, text="Return", command=ret).grid(row=1, column=4)

tk.Label(root, text="Search:").grid(row=2, column=0)
e_search = tk.Entry(root);e_search.grid(row=2, column=1)
tk.Button(root, text="Search", command=search).grid(row=2, column=2)
tk.Button(root, text="View All", command=refresh).grid(row=2, column=3)

cols = ("ID", "Title", "Author", "Status", "Issued To")
tree = ttk.Treeview(root, columns=cols, show="headings", height=15)
for c in cols: tree.heading(c,text=c)
tree.grid(row=3, column=0, columnspan=5, pady=10)
tree.bind("<ButtonRelease-1>", fill_entries)

refresh()
root.mainloop()


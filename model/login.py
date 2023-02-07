import sqlite3
from tkinter import *

def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users(username, password) VALUES(?,?)''', (username, password))
    conn.commit()
    conn.close()

def check_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    result = c.fetchall()
    conn.close()
    return result

def login():
    username = entry_username.get()
    password = entry_password.get()
    result = check_user(username, password)
    if result:
        label_result['text'] = 'Login successful'
    else:
        label_result['text'] = 'Login failed'

root = Tk()
root.title('Login Page')

label_username = Label(root, text='Username')
label_username.grid(row=0, column=0)
entry_username = Entry(root)
entry_username.grid(row=0, column=1)

label_password = Label(root, text='Password')
label_password.grid(row=1, column=0)
entry_password = Entry(root, show='*')
entry_password.grid(row=1, column=1)

button_login = Button(root, text='Login', command=login)
button_login.grid(row=2, column=0)

label_result = Label(root, text='')
label_result.grid(row=2, column=1)

create_table()

root.mainloop()

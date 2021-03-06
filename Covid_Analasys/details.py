from tkinter import *
import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
from covid_api import root

# getting details from db

full_name = StringVar()
id = IntVar()


def delete_record():
    conn = sql.connect('covid_analasys.db')
    cors = conn.cursor()
    cors.execute('delete from patients where id=?', (id.get(),))
    conn.commit()
    conn.close()
    pass


class Details:
    title = Label(root, text="Patient Details", width=20, font=("bold", 20), bg="light blue")
    title.place(x=600, y=60)

    label_0 = Label(root, text="Patient Name", width=20, font=('Ariel', 13), bg="light blue")
    label_0.place(x=600, y=130)
    entry_0 = Entry(root, textvar=full_name)
    entry_0.place(x=775, y=130)


    def get_details(self):
        label_1 = Label(root, text="To delete a record enter ID", width=20, font=('Ariel', 10), bg="light blue")
        label_1.place(x=600, y=130)
        entry_1 = Entry(root, textvar=id)
        entry_1.place(x=775, y=130)
        Button(root, text='Delete', width=5, bg="red", fg='white', command=delete_record).place(x=925, y=130)

        conn = sql.connect('covid_analasys.db')
        cors = conn.cursor()
        cors.execute('SELECT * FROM patients WHERE fullname=?', (full_name.get(),))
        rows = cors.fetchall()
        conn.close()

        frm = Frame(root)
        frm.pack(side=tk.LEFT, padx=5)

        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="5")
        tv.pack()

        tv.heading(1, text="ID")
        tv.column(1, minwidth=0, width=50, stretch=NO)

        tv.heading(2, text="Name")
        tv.column(2, minwidth=0, width=150, stretch=NO)

        tv.heading(3, text="Address")
        tv.column(3, minwidth=0, width=100, stretch=NO)

        tv.heading(4, text="District")
        tv.column(4, minwidth=0, width=100, stretch=NO)

        tv.heading(5, text="Contact")
        tv.column(5, minwidth=0, width=100, stretch=NO)

        tv.heading(6, text="Start_Date")
        tv.column(6, minwidth=0, width=100, stretch=NO)

        tv.heading(7, text="End_Date")
        tv.column(7, minwidth=0, width=100, stretch=NO)

        for i in rows:
            tv.insert('', 'end', values=i)

    Button(root, text='Search', width=5, bg="blue", fg='white', command=get_details).place(x=925, y=130)










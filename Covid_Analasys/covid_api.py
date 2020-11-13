from sqlite3 import IntegrityError
from tkinter import *
from tkcalendar import Calendar,DateEntry
from datetime import datetime
import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
import update

# here you can register

root = Tk()
root.geometry("1200x550")
root.title('Covid Patients')
root.configure(background = "light blue")
label_0 = Label(root,text="Patient's Enrollment", width=20,font=("bold",20),bg="light blue")
label_0.place(x=90,y=60)

full_name = StringVar()
address = StringVar()
d = StringVar()
contact = IntVar()

def details_form():
    def database():
        fn = full_name.get()
        ad = address.get()
        dis = d.get()
        cont = contact.get()
        sd = start_date.get()
        ed = end_date.get()
        try:
            conn = sql.connect('covid_analasys.db')
            cur = conn.cursor()
            cur.execute("insert into patients(fullname, address, district, contact, start_date, end_date) "
                        "values (?,?,?,?,?,?)", (fn, ad, dis, cont, sd, ed))
            conn.commit()
            conn.close()
        except IntegrityError:
            return 'Invalid Input'

    label_1 = Label(root, text="FullName", width=20, font=("bold", 10), bg="light blue")
    label_1.place(x=70, y=130)
    entry_1 = Entry(root, textvar=full_name)
    entry_1.place(x=240, y=130)

    label_2 = Label(root, text="Address", width=20, font=("bold", 10), bg="light blue")
    label_2.place(x=70, y=180)
    entry_2 = Entry(root, textvar=address)
    entry_2.place(x=240, y=180)

    label_3 = Label(root, text="Districts", width=20, font=("bold", 10), bg="light blue")
    label_3.place(x=70, y=230)
    list_of_districts = ['Chennai', 'Kanchipuram', 'Chengalpet', 'Tiruvallur']
    droplist = OptionMenu(root, d, *list_of_districts)
    droplist.config(width=15)
    d.set('Select your District')
    droplist.place(x=240, y=230)

    label_4 = Label(root, text="Contact", width=20, font=("bold", 10), bg="light blue")
    label_4.place(x=70, y=280)
    entry_4 = Entry(root, textvar=contact)
    entry_4.place(x=240, y=280)

    label_5 = Label(root, text="Start Date", width=20, font=("bold", 10), bg="light blue")
    label_5.place(x=70, y=330)
    start_date = DateEntry(root, width=30, bg="darkblue", fg="white", date_pattern='dd/mm/yyyy')
    start_date.grid()
    start_date.place(x=240, y=330)

    label_6 = Label(root, text="End Date", width=20, font=("bold", 10), bg="light blue")
    label_6.place(x=70, y=380)
    end_date = DateEntry(root, width=30, bg="darkblue", fg="white", day=datetime.now().day + 10,
                         date_pattern='dd/mm/yyyy')
    end_date.grid()
    end_date.place(x=240, y=380)

    Button(root, text='Enroll', width=20, bg="blue", fg='white', command=database).place(x=180, y=450)

details_form()

f_name = StringVar()
id = IntVar()
id_update = IntVar()

def update_record():
    ud = StringVar()
    root.destroy()
    if id_update.get() >=1:
        def database():
            un = entry_1.get()
            ua = entry_2.get()
            dis = ud.get()
            uc = entry_4.get()
            sd = start_date_update.get()
            ed = end_date_update.get()
            id_u = id_update.get()
            try:
                conn = sql.connect('covid_analasys.db')
                cur = conn.cursor()
                cur.execute("Update patients set fullname = ?, address = ?, district = ?, contact = ?, start_date = ?, end_date = ? where id = ?",(un,ua,dis,uc,sd,ed,id_u))
                conn.commit()
                conn.close()
                root1.destroy()
            except IntegrityError:
                return 'Invalid Input'

        root1 = Tk()
        root1.geometry("550x500")
        root1.title('Covid Patients')
        root1.configure(background="light blue")
        label_0 = Label(root1, text="Update Patient Details", width=20, font=("bold", 20), bg="light blue")
        label_0.place(x=90, y=60)

        label_1 = Label(root1, text="FullName", width=20, font=("bold", 10), bg="light blue")
        label_1.place(x=70, y=130)
        entry_1 = Entry(root1)
        entry_1.grid()
        entry_1.place(x=240, y=130)

        label_2 = Label(root1, text="Address", width=20, font=("bold", 10), bg="light blue")
        label_2.place(x=70, y=180)
        entry_2 = Entry(root1)
        entry_2.grid()
        entry_2.place(x=240, y=180)

        label_3 = Label(root1, text="Districts", width=20, font=("bold", 10), bg="light blue")
        label_3.place(x=70, y=230)
        list_of_districts = ['Chennai', 'Kanchipuram', 'Chengalpet', 'Tiruvallur']
        districts = OptionMenu(root1, ud, *list_of_districts)
        districts.config(width=15)
        ud.set('Select your District')
        districts.place(x=240, y=230)

        label_4 = Label(root1, text="Contact", width=20, font=("bold", 10), bg="light blue")
        label_4.place(x=70, y=280)
        entry_4 = Entry(root1)
        entry_4.grid()
        entry_4.place(x=240, y=280)

        label_5 = Label(root1, text="Start Date", width=20, font=("bold", 10), bg="light blue")
        label_5.place(x=70, y=330)
        start_date_update = DateEntry(root1, width=30, bg="darkblue", fg="white", date_pattern='dd/mm/yyyy')
        start_date_update.grid()
        start_date_update.place(x=240, y=330)

        label_6 = Label(root1, text="End Date", width=20, font=("bold", 10), bg="light blue")
        label_6.place(x=70, y=380)
        end_date_update = DateEntry(root1, width=30, bg="darkblue", fg="white", day=datetime.now().day + 10,
                                    date_pattern='dd/mm/yyyy')
        end_date_update.grid()
        end_date_update.place(x=240, y=380)

        Button(root1, text='Update', width=20, bg="orange", fg='white', command=database).place(x=180, y=450)
        root1.mainloop()
    else:
        pass


def delete_record():
    conn = sql.connect('covid_analasys.db')
    cors = conn.cursor()
    cors.execute('delete from patients where id=?', (id.get(),))
    conn.commit()
    conn.close()
    root.destroy()

title = Label(root, text="Patient Details", width=20, font=("bold", 20), bg="light blue")
title.place(x=600, y=50)

label_0 = Label(root, text="Patient Name", width=20, font=('Ariel', 13), bg="light blue")
label_0.place(x=600, y=100)
entry_0 = Entry(root, textvar=f_name)
entry_0.place(x=775, y=100)

def get_details():
    update = Label(root, text="To Update a record enter ID", width=20, font=('Ariel', 10), bg="light blue")
    update.place(x=600, y=150)
    update_entry = Entry(root, textvar=id_update)
    update_entry.place(x=775, y=150)
    Button(root, text='Update', width=5, bg="orange", fg='white', command=update_record).place(x=925, y=150)


    delete = Label(root, text="To delete a record enter ID", width=20, font=('Ariel', 10), bg="light blue")
    delete.place(x=600, y=200)
    delete_entry = Entry(root, textvar=id)
    delete_entry.place(x=775, y=200)
    Button(root, text='Delete', width=5, bg="red", fg='white', command=delete_record).place(x=925, y=200)

    conn = sql.connect('covid_analasys.db')
    cors = conn.cursor()
    cors.execute('SELECT * FROM patients WHERE fullname=?', (f_name.get(),))
    rows = cors.fetchall()
    conn.close()

    frm = Frame(root)
    # frm.pack(side=tk.BOTTOM, padx=5)
    frm.place(x=500,y=300)
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

    chennai = []
    kanchipuram = []
    changalpet = []
    tiruvallur = []

    for i in rows:
        tv.insert('', 'end', values=i)
        if i[3] == 'Chennai':
            chennai.append(i)
        elif i[3] == 'Kanchipuram':
            kanchipuram.append(i)
        elif i[3] == 'Changalpet':
            changalpet.append(i)
        else:
            tiruvallur.append(i)

    if chennai or kanchipuram or changalpet or tiruvallur:
        total_districts = Label(root, text="Total no of districts : ", width=20, font=('Ariel', 10), bg="light blue")
        total_districts.place(x=500, y=250)
        c = Label(root, text="Chennai:"+str(len(chennai)), width=10, font=('Ariel', 10), bg="light blue")
        c.place(x=640, y=250)
        k = Label(root, text="Kanchipuram:" + str(len(kanchipuram)), width=10, font=('Ariel', 10), bg="light blue")
        k.place(x=730, y=250)
        chan = Label(root, text="Changalpet:" + str(len(changalpet)), width=10, font=('Ariel', 10), bg="light blue")
        chan.place(x=830, y=250)
        t = Label(root, text="Tiruvallur:" + str(len(tiruvallur)), width=10, font=('Ariel', 10), bg="light blue")
        t.place(x=930, y=250)

Button(root, text='Search', width=5, bg="blue", fg='white', command=get_details).place(x=925, y=100)

root.mainloop()
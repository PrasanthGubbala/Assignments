from sqlite3 import IntegrityError
from tkinter import *
from tkcalendar import Calendar,DateEntry
from datetime import datetime
import sqlite3 as sql

# here you can register

root = Tk()
root.geometry("500x550")
root.title('Patient Registration')
root.configure(background = "light blue")
label_0 = Label(root,text="Patient's Enrollment", width=20,font=("bold",20),bg="light blue")
label_0.place(x=90,y=60)

full_name = StringVar()
address = StringVar()
d = StringVar()
contact = IntVar()


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
                    "values (?,?,?,?,?,?)",(fn, ad, dis, cont, sd, ed))
        conn.commit()
        conn.close()
    except IntegrityError:
        return 'Invalid Input'

label_1 = Label(root,text="FullName", width=20,font=("bold",10),bg="light blue")
label_1.place(x=70,y=130)
entry_1 = Entry(root,textvar=full_name)
entry_1.place(x=240,y=130)

label_2 = Label(root,text="Address", width=20,font=("bold",10),bg="light blue")
label_2.place(x=70,y=180)
entry_2 = Entry(root, textvar=address)
entry_2.place(x=240,y=180)

label_3 = Label(root,text="Districts",width=20,font=("bold",10),bg="light blue")
label_3.place(x=70,y=230)
list_of_districts = [ 'Chennai' ,'Kanchipuram' , 'Chengalpet' ,'Tiruvallur']
droplist = OptionMenu(root, d, *list_of_districts)
droplist.config(width=15)
d.set('Select your District')
droplist.place(x=240,y=230)

label_4 = Label(root,text="Contact", width=20,font=("bold",10),bg="light blue")
label_4.place(x=70,y=280)
entry_4 = Entry(root, textvar=contact)
entry_4.place(x=240,y=280)

label_5 = Label(root,text="Start Date", width=20,font=("bold",10),bg="light blue")
label_5.place(x=70,y=330)
start_date = DateEntry(root,width=30,bg="darkblue",fg="white",date_pattern='dd/mm/yyyy')
start_date.grid()
start_date.place(x=240,y=330)


label_6 = Label(root,text="End Date", width=20,font=("bold",10),bg="light blue")
label_6.place(x=70,y=380)
end_date = DateEntry(root,width=30,bg="darkblue",fg="white",day=datetime.now().day+10,date_pattern='dd/mm/yyyy')
end_date.grid()
end_date.place(x=240,y=380)

Button(root, text='Enroll' , width=20,bg="blue",fg='white',command=database).place(x=180,y=450)

root.mainloop()
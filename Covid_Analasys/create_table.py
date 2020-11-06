import sqlite3 as sql
# for creating table
conn = sql.connect('covid_analasys.db')
cors = conn.cursor()
cors.execute("CREATE TABLE patients(id INTEGER PRIMARY KEY AUTOINCREMENT,fullname text,address text,district text,contact int ,start_date text,end_date text)")
conn.close()
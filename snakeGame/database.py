import sqlite3 as sql

conn = sql.connect('leaderBoard.db')
cors = conn.cursor()
cors.execute('create table leader_board(score int)')
conn.close()
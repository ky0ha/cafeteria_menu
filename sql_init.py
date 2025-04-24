import sqlite3

db = sqlite3.connect("base.db")
cursor = db.cursor()

cursor.execute("""create table if not exists menus(
    f_id integer primary key autoincrement,
    f_name text not null,
    f_taste text not null,
    f_type text not null,
    f_meator text not null)""")

cursor.execute("""create table if not exists records(
    f_id int not null,
    c_id int not null,
    update_time datetime default CURRENT_TIMESTAMP,
    primary key(f_id, c_id))""")

cursor.execute("""create table if not exists cookers(
    c_id integer primary key autoincrement,
    c_name text not null,
    create_time datetime default CURRENT_TIMESTAMP)""")

db.commit()
db.close()
# import sqlite3

# db = sqlite3.connect("base.db")
# cursor = db.cursor()

# cursor.execute("""create table if not exists menus(
#     f_id integer primary key autoincrement,
#     f_name text not null,
#     f_taste text not null,
#     f_type text not null,
#     f_meator text not null)""")

# cursor.execute("""create table if not exists records(
#     f_id int not null,
#     c_id int not null,
#     update_time datetime default CURRENT_TIMESTAMP,
#     primary key(f_id, c_id))""")

# cursor.execute("""create table if not exists cookers(
#     c_id integer primary key autoincrement,
#     c_name text not null,
#     create_time datetime default CURRENT_TIMESTAMP)""")

# db.commit()
# db.close()

from sql_manager import SQLManager

sql = SQLManager()

with sql:
    sql.create_table(
        "menus",
        [
            "f_id integer primary key autoincrement",
            "f_name text not null",
            "f_taste text not null",
            "f_type text not null",
            "f_meator text not null",
        ],
    )
    
    sql.create_table(
        "records",
        [
            "f_id int not null",
            "c_id int not null",
            "update_time datetime default CURRENT_TIMESTAMP",
            "primary key(f_id, c_id)",
        ],
    )

    sql.create_table(
        "cookers",
        [
            "c_id integer primary key autoincrement",
            "c_name text not null",
            "create_time datetime default CURRENT_TIMESTAMP",
        ],
    )
    
    sql.insert_into_table(
        "menus",
        [100, 'a', '', '', ''],
        key = ["f_id", "f_name", "f_taste", "f_type", "f_meator"]
    )
    
    sql.delete_from_table("menus", "f_id = 100")
    
    sql.insert_into_table(
        "records",
        [100, 1000],
        key = ["f_id", "c_id"]
    )

    sql.delete_from_table("records", "f_id = 100 and c_id = 1000")
    
    sql.insert_into_table(
        "cookers",
        [1000, 'a'],
        key = ["c_id", "c_name"]
    )
    
    sql.delete_from_table("cookers", "c_id = 1000")
    
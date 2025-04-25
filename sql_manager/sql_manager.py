import sqlite3

class SQLManager:
    def __init__(self, db_name='base.db'):
        self.conn = sqlite3.connect(db_name)
    
    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def close(self):
        if self.cursor:
            self.cursor.close()

    def create_table(self, table_name, columns):
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.cursor.execute(create_table_query)
        self.conn.commit()
    
    def insert_into_table(self, table_name, values, key=None):
        if isinstance(key, list):
            insert_query = f"INSERT INTO {table_name} ({', '.join(key)}) VALUES ({', '.join(['?'] * len(values))})"
        elif isinstance(key, str):
            insert_query = f"INSERT INTO {table_name} ({key}) VALUES ({', '.join(['?'] * len(values))})"
        else:
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(values))})"
        self.cursor.execute(insert_query, values)
        self.conn.commit()
    
    def select_from_table(self, table_name, columns, condition=None, prefix=None):
        select_query = f"SELECT {', '.join(columns)} FROM {table_name}"
        if prefix:
            select_query = prefix + select_query
        if condition:
            select_query += f" WHERE {condition}"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def update_table(self, table_name, set_clause, condition):
        update_query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(update_query)
        self.conn.commit()

    def delete_from_table(self, table_name, condition):
        delete_query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(delete_query)
        self.conn.commit()
    
    def complex_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

if __name__ == "__main__":
    sql = SQLManager("base.db")
    with sql:
        # sql.insert_into_table(
        #     "cookers", 
        #     ['mike', 'CURRENT_TIMESTAMP'],
        #     key=['c_name', 'create_time']
        # )
        # sql.delete_from_table('cookers', 'c_name = "mike"')
        pass
        
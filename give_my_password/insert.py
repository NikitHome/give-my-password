import sqlite3
import os.path

class Insert():
    def insert(self):
        self.push_name = input("Введите название сервиса: ")
        self.login = input("Введите логин: ")
        self.password = input("Введите пароль: ")
        
    def insert_data(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "sqlite3.db")
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS services(
            service TEXT,
            login TEXT,
            password TEXT);

        """)
        connect.commit()
        
        service_info = (self.push_name, self.login, self.password)
        cursor.execute("INSERT INTO services VALUES(?, ?, ?);", service_info)
        connect.commit()
        
        print("Данные сохранены!")
import sqlite3
import os.path

class Receive():
    def receive(self):
        self.take_name = input("Введите название сервиса: ")
        
    def receive_data(self):   
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "sqlite3.db")
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        
        cursor.execute("SELECT * FROM services;")
        all_results = cursor.fetchall() 
        
        for result in all_results:
            if result[0].lower() == self.take_name.lower():
                print(result[1])
                print(result[2])
            else:
                print("Данные не найдены...")
import sqlite3
import os.path

class Delete():        
    def delete(self):
        self.delete_name = input("Введите название сервиса: ")
        
    def delete_data(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "sqlite3.db")
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        
        cursor.execute(f"DELETE FROM services WHERE service='{self.delete_name}'")
        connect.commit()
        
        print("Данные удалены!")
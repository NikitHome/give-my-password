import sqlite3
import os.path

class DeleteAll():
    def delete_all_data(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "sqlite3.db")
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        
        cursor.execute("DELETE FROM services;")
        connect.commit()
        
        print("Все данные удалены!")
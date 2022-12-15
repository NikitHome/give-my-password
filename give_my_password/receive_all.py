import sqlite3
import os.path

class ReceiveAll():
    def receive_all_data(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "sqlite3.db")
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        
        cursor.execute("SELECT * FROM services;")
        all_results = cursor.fetchall()
        
        for result in all_results:
            print(f"{result[0]}:")
            print(f"\t{result[1]}")
            print(f"\t{result[2]}") 
from insert import Insert
from receive import Receive
from delete import Delete
from colors import Colors
from receive_all import ReceiveAll
from delete_all import DeleteAll


insert = Insert()
receive = Receive()
delete = Delete()
receive_all = ReceiveAll()
delete_all = DeleteAll()

def start():
        none = Colors.none
        green = Colors.green
        yellow = Colors.yellow
        red = Colors.red
        
        print("Добавить (1) / Получить (2) / Получить всё (3) / Удалить (4) / Удалить всё (5)")
        select = input()
        
        return select


while True:
    def start():
        none = Colors.none
        green = Colors.green
        yellow = Colors.yellow
        red = Colors.red
        
        print("Добавить (1) / Получить (2) / Получить всё (3) / Удалить (4) / Удалить всё (5)")
        select = input()
        
        return select
    
    start = start()

    if start == "1":
        insert.insert()
        insert.insert_data()
    elif start == "2":
        receive.receive()
        receive.receive_data()
    elif start == "3":
        receive_all.receive_all_data()
    elif start == "4":
        delete.delete()
        delete.delete_data()
    elif start == "5":
        delete_all.delete_all_data()
    else:
        print("Error")
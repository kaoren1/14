import sqlite3
import function

conn = sqlite3.connect("database2.db")
cursor = conn.cursor()

class AdminFunctional:
    @staticmethod
    def Create():
        while True:
            try:
                NameService = str(input("Введите название услуги: "))
                Price = int(input("Введите цену: "))
                cursor.execute("INSERT INTO Service (NameService, Price) VALUES (?,?)", (NameService, Price))
                conn.commit()
                break
            except ValueError:
                print("Ошибка ввода данных")

        while True:
            try:
                SurnameMaster = str(input("Введите фамилию мастера: "))
                NameMaster = str(input("Введите имя мастера: "))
                cursor.execute("INSERT INTO Master (SurnameMaster, NameMaster) VALUES (?, ?)", (SurnameMaster, NameMaster))
                conn.commit()
                break
            except ValueError:
                print("Ошибка ввода данных")

        while True:
            try:
                Duration = float(input("Введите время услуги (в часах) : "))
                cursor.execute("INSERT INTO SessionTime (Duration) VALUES (?)", (Duration,))
                conn.commit()
                break
            except ValueError:
                print("Ошибка ввода данных")

        while True:
            try:
                Street = str(("Введите адрес: "))
                cursor.execute("INSERT INTO Building (Street) VALUES (?)", (Street,))
                conn.commit()
                break
            except ValueError:
                print("Ошибка ввода данных")
        conn.commit()
        function.AdminFunction()

    @staticmethod
    def Delete():
        while True:
            try:
                cursor.execute("SELECT * FROM Service")
                id = int(input("Введите id для удаления услуги и всех её данных: "))
                cursor.execute("DELETE FROM Service WHERE ID_Service = ?", (id,))
                conn.commit()
                function.AdminFunction()
                break
            except ValueError:
                print("Введен неправильный id")

    @staticmethod
    def Update():
        cursor.execute("SELECT * FROM Service")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        id = input("Введите id услуги для её изменения: ")
        NewName = input("Введите новое имя услуги: ")
        cursor.execute("UPDATE Service SET NameService = ? WHERE ID_service = ?", (NewName, id))
        conn.commit()
        function.AdminFunction()

class UserFunctional(AdminFunctional):
    @staticmethod
    def Filter():
        cursor.execute("SELECT * FROM Service")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        while True:
            try:
                print("Доступные фильтры: 1. Цена")
                a = int(input("Выберите фильтр: "))
                if a == 1:
                    break
                else:
                    print("Введен неправильный фильтр")
            except ValueError:
                print("Введен неправильный фильтр")
        if a == 1:
            while True:
                try:
                    Price = float(input("Введите максимальную цену: "))
                    cursor.execute("SELECT * FROM Service WHERE Price < ?", (Price,))
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                    function.UserFunction()
                    break
                except ValueError:
                    print("Введена неправильная цена")

    @staticmethod
    def Select():
        cursor.execute("SELECT * FROM Service")
        while True:
            try:
                id = int(input("Введите id услуги для выбора: "))
                cursor.execute("SELECT * FROM Service WHERE ID_Service = ?", (id,))
                function.UserFunction()
                break
            except ValueError:
                print("Введен некорректный id")
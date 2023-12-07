from function import AdminFunction, UserFunction

class Authorization:
    def __init__(self, basa):
        self.__basa = basa
    def login(self, user, password):
        if user in self.__basa and self.__basa[user] == password:
            if user == "admin" and password == "admin123":
                print("Добро пожаловать")
                return AdminFunction()
            else:
                print("Успешный вход")
                return UserFunction()
        else:
            print("Неверное имя пользователя или пароль")

class Registration:
    def __init__(self, basa):
        self.__basa = basa
    def register(self, user, password):
        if user in self.__basa:
            print("Пользователь с таким именем уже существует")
        else:
            print("Успешная регистрация")
            self.__basa[user] = password

basa = {"admin": "admin123"}
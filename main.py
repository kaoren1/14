from reau import Authorization, Registration, basa

authorization = Authorization(basa)
registration = Registration(basa)

while True:
    print("Пройдите авторизацию, чтобы продолжить.")
    print("1. Авторизация")
    print("2. Регистрация")
    print("3. Выйти")

    while True:
        try:
            a = int(input("Выберите действие: "))
            if 1 <= a <= 3:
                break
        except ValueError:
            print("Введено неправильное действие. Попробуйте снова")

    if a == 1:
        user = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        authorization.login(user, password)
        break
    elif a == 2:
        user = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        registration.register(user, password)
    elif a == 3:
        print("Завершение выполнения программы")
        exit()
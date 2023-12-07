from crud import AdminFunctional, UserFunctional
def AdminFunction():
    print()
    print("1. Создание услуги тату-салона")
    print("2. Удаление уже созданной услуги")
    print("3. Изменение уже существующей услуги")
    print("4. Выход")
    while True:
        try:
            function = int(input("Выберите функцию: "))
            if 1 <= function <= 4:
                break
        except ValueError:
            print("Введено неправильное действие. Попробуйте снова")
    match function:
        case 1:
            AdminFunctional.Create()
        case 2:
            AdminFunctional.Delete()
        case 3:
            AdminFunctional.Update()
        case 4:
            exit()

def UserFunction():
    print()
    print("1. Фильтрация услуг")
    print("2. Выбор услуги")
    print("3. Выход")
    while True:
        try:
            function = int(input("Выберите функцию: "))
            if 1 <= function <= 3:
                break
        except ValueError:
            print("Введено неправильное действие. Попробуйте снова")
    match function:
        case 1:
            UserFunctional.Filter()
        case 2:
            UserFunctional.Select()
        case 3:
            exit()
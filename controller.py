import view as v
import Logger_export as exp
import logger_reader as r


def start():
    print('='*25)
    print("0: Показать телефонный справочник ")
    print("1: Импортировать данные из файла .json ")
    print("2: Импортировать данные из файла .csv")
    print("3: Введите нового пользователя ")
    print("4: Экспортировать данные в файл .csv ")
    print("5: Экспортировать данные в файл .json ")
    print("6: Выйти из меню")
    button = int(input("Выберите пункт меню: "))
    if button == 0:
        Show_phone_book()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button == 1:
        Import_data_json()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button == 2:
        Import_data_csv()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button == 3:
        Add_new_contact()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button == 4:
        Export_data_csv()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button == 5:
        Export_data_json()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button ==6:
        exit()

def Show_phone_book():
    return r.Show()

def Import_data_json():
     return r.Read_data_json()

def Import_data_csv():
     return r.Read_data_csv()

def Add_new_contact():
    return r.Add_position(v.New_employee())

def Export_data_csv():
     return exp.Export_data_csv(r.Read_data_txt())


def Export_data_json():
     return exp.Export_data_json(r.Read_data_txt())
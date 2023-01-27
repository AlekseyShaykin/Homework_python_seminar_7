import csv 
import json

def Show():
    with open('PYTHON\Homework_seminar_7\phone_book.txt', 'r') as csv_file: 
      line = csv.reader(csv_file)
      print('='*25)
      for i in line: 
         print(*i)
      print('='*25)


# считывание данных с файла для вклчения в методы экспорта

def Read_data_csv():
    with open('PYTHON\Homework_seminar_7\phone_book.csv') as csv_file: 
      line = csv.reader(csv_file)
      for i in line:
        print(*i)
      line = list(line)
      return line

# Read_data_csv()
# считывание данных с файла json

def Read_data_json():
    with open("PYTHON\Homework_seminar_7\phone_book.json", "r") as json_file:
        reader = json_file.read()
        i = json.loads(reader)     #Функция json.loads взяла строку capitals_json и на основе её данных сделала словарь. Теперь в capitals лежит не строка, а словарь:
        print(*i)
        return reader




def Read_data_txt():                      #сначала считываем данные из файла csv (можно txt указать)
    with open('PYTHON\Homework_seminar_7\phone_book.txt') as file:     
        reader = csv.reader(file) 
        reader = list(reader)   #преобразуем список в список списков для того, чтобы можно было его записать в другой csv файл в нормальном виде
        # print(reader)
        return reader



def Add_position(element):
    name, surname, status, number =element
    with open('PYTHON\Homework_seminar_7\phone_book.txt','a') as text:
        element = f'{name};{surname};{status};{number}'
        text.write(str(f'\n{element}'))



# считывание данных с файла txt:

# def Read_data_txt():
#     with open('PYTHON\Homework_seminar_7\phone_book.txt', 'r') as file:
#         line = file.read().strip().split('\n')
#         line= list(line)                                       #преобразовываем список line в список списков для экспорта в csv и json
#         return (list(line))
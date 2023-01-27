import json
import csv




def Export_data_csv(reader):    # метод по экспорту данных в csv файл
    myFile = open('PYTHON\Homework_seminar_7\Export_data_csv.csv', 'w')  
    with myFile:
      writer = csv.writer(myFile)
      writer.writerows(reader)
      print("File has written as .csv")



def Export_data_json(reader):
    data_json = json.dumps(reader)     # из словаря делаем строку
    with open("PYTHON\Homework_seminar_7\Export_data_json.json", "w") as my_file:
       my_file.write(data_json)
       print("File has written as .json")






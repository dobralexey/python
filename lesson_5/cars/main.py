# coding: utf-8
# python 3.4

#1
import sys

try:
    from db import load_pickle, save_pickle
    from debug import data_output, power_value_search, power_gap_search, name_search
except ImportError:
    print ("Проверьте правильность написания модуля или функций, которые Вы хотите использовать")
    sys.exit(0)



def db_path():     # Функция ввода пути до БД или её создания по этому пути

    try:
        path = input("Введите путь до базы данных и её название: ")
    except KeyboardInterrupt:
        print ("Ошибка сочетания клавиш, введите путь до файла")
    return path

def com_input():    # Функция ввода команды

    command = input ('Ввести или Вывести информацию о машине? (Для окончания сеанса введите "Стоп")')
    return command


def com_check (command):    # Функия проверки правильности ввода команды
    
    if command == 'Ввести' or command == 'Вывести' or command == "Стоп":
        return command
    else:
        print ('Вы ошибились в написании ввода команды, нужно писать "Ввести" или "Вывести"')


def data_input(data_car, path):    # Функция ввода данных пользователем    
    
            car_input = input("Введите марку автомобиля: ")
            if car_input.isalpha() == False:
                print ("Вы ошиблись, марка может состоять только из букв!")
                
            power_input = input ("Введите мощность двигателя: " )
            if power_input.isdigit() == False:
                print ("Вы ошиблись, мощность может состоять только из цифр!")
                
            data_car [car_input] = power_input
            
            save_pickle(data_car, path)
            

def main_prog (path, command):    # Функция программы
    
    data_car = load_pickle(path)
    while command != "Стоп":
        if command == "Ввести":
            data_input(data_car, path)
        elif command == "Вывести":
            data_output(data_car)
        command = com_check(com_input())
        
    power_value_search(data_car)
    power_gap_search(data_car)
    name_search(data_car)


main_prog(db_path(),com_check(com_input())) # Тест  программы

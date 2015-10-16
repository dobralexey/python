# coding: utf-8

import pickle
path = input ("Введите путь, куда сохранить базу данных автомобилей, или где она сохранена :")
try:
    with open (path + '/data_car.pickle', 'rb') as f:
        data_car = pickle.load(f)
except:
    data_car = {}

car_q = "Ввести"    # Цикл для ввода автомобилей
while car_q == "Ввести":
    car_q = input ("Ввести или Вывести информацию о машине? :")
    if car_q == "Ввести":
        with open (path + '/data_car.pickle', 'wb') as f:
            car_input = input("Введите марку автомобиля: ")
            if car_input.isalpha() == False:
                print ("Вы ошиблись, марка может состоять только из букв!")
            power_input = input ("Введите мощность двигателя: " )
            if power_input.isdigit() == False:
                print ("Вы ошиблись, мощность может состоять только из цифр!")
            data_car [car_input] = power_input
            pickle.dump (data_car, f)
            
    if car_q == "Вывести":    # Цикл для вывода автомобилей
        with open (path + '/data_car.pickle', 'rb') as f:
            data_car = pickle.load(f)
            data_car_defsort = sorted (data_car)
            print (data_car_defsort)
            for key in sorted(data_car, key=lambda key: int((data_car[key])), reverse = True):
                print(key, data_car[key])
                
        power_input = int(input ("Введите значение мощности для поиска :"))    # Поиск по значению мощности
        data_car_lst = []
        for key in data_car:
            if  int(data_car[key]) == power_input :
                    data_car_lst.append([key,data_car[key]])
        print ("Машины с данной мощностью :", data_car_lst)
        data_car_lst = []
        for key in data_car:
            if int(data_car[key]) > power_input:
                data_car_lst.append([key,data_car[key]])
        print ("Машины с большей мощностью :", data_car_lst)
        data_car_lst = []
        for key in data_car:
            if int(data_car[key]) < power_input:
                data_car_lst.append([key,data_car[key]])
        print ("Машины с меньшей мощностью :", data_car_lst)
            
        power_input = input ("Введите промежуток мощности для поиска:")    # Поиск по промежутку мощности
        power_lst = power_input.split('-')
        data_car_lst = []
        for key in data_car:
            if int(power_lst[0])<=int(data_car[key])<=int(power_lst[1]):
                data_car_lst.append([key,data_car[key]])
        print ("Машины в заданном промежутке мощности :", data_car_lst)

        name_input = input ("Введите название марки или часть названия: ")

        for key in data_car:
            if name_input in key:
                print ("Машины, где встречается часть названия :", key, data_car[key])
        for key in data_car:
            if name_input == key:
                print ("Машины, полностью соответствующие заданому имени", key, data_car[key])
            
                   
                

        



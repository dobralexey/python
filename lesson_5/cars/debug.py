# coding: utf- 8
# python 3.4

def data_output(data_car):    # Функция вывода данных пользователю
    print(data_car)


def power_value_search(data_car):    # Функия поиска автомобиля по значению мощности (пытался уменьшить=))
    try:
        power_input = int(input ("Введите значение мощности для поиска :"))
    except ValueError:
        print ("Необходтимо ввести число без единиц измерения и в виде цифр")
        power_input = int(input ("Введите значение мощности для поиска :"))
    
    
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



def power_gap_search(data_car):    # Функция поиска автомобиля по промежутку мощности

    try:
        power_input = input ("Введите промежуток мощности для поиска:")
        power_lst = power_input.split('-')
    except ValueError:
        print ('Необходимо ввести промежуток мощности в виде "50-60"')
        power_input = input ("Введите промежуток мощности для поиска:")
        power_lst = power_input.split('-')

    data_car_lst = []
    for key in data_car:
        if int(power_lst[0])<=int(data_car[key])<=int(power_lst[1]):
            data_car_lst.append([key,data_car[key]])
    print ("Машины в заданном промежутке мощности :", data_car_lst)

            
def name_search(data_car):    # Функция поска автомобиля по названию
    
    name_input = input ("Введите название марки или часть названия: ")

    for key in data_car:
        if name_input in key:
            print ("Машины, где встречается часть названия :", key, data_car[key])
        if name_input == key:
            print ("Машины, полностью соответствующие заданому имени", key, data_car[key])

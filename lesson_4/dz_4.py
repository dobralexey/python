# coding: utf-8
# python 3.4

#1

def db_path():     # Функция ввода пути до БД или её создания по этому пути
    
    path = input("Введите путь до базы данных и её название: ")
    return path

def com_input():    # Функция ввода команды
    
    command = input ('Ввести или Вывести информацию о машине? (Для окончания сеанса введите "Стоп")')
    return command


def com_check (command):    # Функия проверки правильности ввода команды
    
    if command == 'Ввести' or command == 'Вывести' or command == "Стоп":
        return command
    else:
        print ('Вы ошибились в написании ввода команды, нужно писать "Ввести" или "Вывести"')


def load_pickle(path):    # Функция загрузки базы данных
    
    import pickle 
    try:
        with open (path, 'rb') as f:
            data_car = pickle.load(f)
    except IOError:
        data_car = {}
    return data_car


def save_pickle(data_car, path):    # Функция сохранения в базу данных
    
    import pickle
    with open (path, 'wb') as f:
        pickle.dump (data_car, f)
    f.close()


def data_input(data_car, path):    # Функция ввода данных пользователем    
    
            car_input = input("Введите марку автомобиля: ")
            if car_input.isalpha() == False:
                print ("Вы ошиблись, марка может состоять только из букв!")
                
            power_input = input ("Введите мощность двигателя: " )
            if power_input.isdigit() == False:
                print ("Вы ошиблись, мощность может состоять только из цифр!")
                
            data_car [car_input] = power_input
            
            save_pickle(data_car, path)


def data_output(data_car, path):    # Функция вывода данных пользователю
    
        print(data_car)



def power_value_search(data_car):    # Функия поиска автомобиля по значению мощности (пытался уменьшить=))
    
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
            

def main_prog (path, command):    # Функция программы
    
    data_car = load_pickle(path)
    while command != "Стоп":
        if command == "Ввести":
            data_input(data_car, path)
        elif command == "Вывести":
            data_output(data_car, path)
        command = com_check(com_input())
        
    power_value_search(data_car)
    power_gap_search(data_car)
    name_search(data_car)


main_prog(db_path(),com_check(com_input())) # Тест 1 варианта программы



#2

def main_prog2 (path, command):    # Функция программы со словарем
    
    data_car = load_pickle(path)
    FUNCS = {'Ввести': data_input, 'Вывести': data_output}
    
    while command != "Стоп":
        FUNCS[command](data_car, path)
        command = com_check(com_input())
        
    power_value_search(data_car)
    power_gap_search(data_car)
    name_search(data_car)


main_prog2(db_path(),com_check(com_input())) # Тест 2 варианта программы



#3

def data_edit(path):    # Функция редактирования мощности машины
    
    data_car = load_pickle(path)
    who_edit = input ("Введите марку машины, которую хотите отредактировать")
    data_car[who_edit] = input ("Введите новое значение для мощности")

    save_pickle(data_car, path)

            
def data_del(path):    # Функция удаления машины

    data_car = load_pickle(path)
    who_del = input ("Введите марку машины, которую хотите удалить")
    del data_car[who_del]

    save_pickle(data_car, path)


data_edit(db_path()) # Тест функции редактирования    
data_del(db_path())  # Тест функции удаления


#4-5

def nomer_coord (path):  # Функция ввода номера и координат
    
    data_car = load_pickle(path)
    
    for key in data_car:
        print ("Машина: ", key) 
        nomer = input ("Введите номер машины")
        coord = input ("Введите координатты x (широта) и y (долгота) (Например : 60.7, 30.1)")
        data_car[key] = (data_car[key], {nomer : (float(coord.split(',')[0]),float(coord.split(',')[1]))})
        
    save_pickle(data_car, path)

nomer_coord(db_path())   # Тест функции добавления координат и номера

def change_coord (path):  # Функция перемены координат

    data_car = load_pickle(path)
    nomer = input ("Введите номер машины")
    coord = input ("Введите новые координаты x (широта) и y (долгота) (Например : 60.7, 30.1) ")
    coord = (float(coord.split(',')[0]), float(coord.split(',')[1]))

    nom_dict = {}      # Создаем словарь , заполняем ключ(номер): значение(координаты)
    for key in data_car:
         nom_dict.update(data_car[key][1])
         
    if coord in nom_dict.values():
        print ("Вы пытаетесь поставить две машины в одни координаты!")
        sys.exit(0)
        
    else:
        for key in data_car:                        # Изменяем координаты во внутреннем словаре, доступ к 
            if nomer in data_car[key][1]:           # значению по ключу;
                old_coord = data_car[key][1][nomer] # Сохраняем старые координаты
                data_car[key][1][nomer]=coord
            
    save_pickle(data_car, path)
    
    return old_coord, coord

    
x = change_coord(db_path())  # Тест функции смены координат 


# 6

def dist_calc (old_coord, coord):
    
    from math import acos, cos, sin, radians
    
    lat_1 = radians(old_coord[0])
    lon_1 = radians(old_coord[1])
    lat_2 = radians(coord[0])
    lon_2 = radians(coord [1])

    dist = 6371 * acos( cos(lat_1) * cos(lat_2) + sin(lat_1) * sin(lat_2) * cos(lon_1 - lon_2) )

    print (dist, "км")
    return dist


x,y = change_coord(db_path())  
dist_calc(x,y)                  # Тест функции расчета расстояния по координатам


    

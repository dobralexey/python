# coding: utf - 8
# python 3.4

import sys

def load_pickle(path):    # Функция загрузки базы данных  

    import pickle 
    try:
        f = open (path, 'rb')
        data_car = pickle.load(f)
    except IOError:
        data_car = {}
    else:
        print ("База данных успешно загружена")
    finally:
        return data_car


def save_pickle(data_car, path):    # Функция сохранения в базу данных
 
    import pickle
    try:
        f = open (path, 'wb')
        pickle.dump (data_car, f)
        f.close()
    except IOError:
        print ("Введен неверный путь сохранения базы данных")
        sys.exit(0)

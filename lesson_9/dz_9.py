#coding: utf-8

from random import randint
from abc import ABCMeta, abstractmethod, abstractproperty


class Prop_of_Anim(metaclass = ABCMeta):    # Абстрактный класс свойств животных
    
    @abstractproperty
    def sound():
        pass
    
    @abstractproperty
    def speed():
        pass

    @abstractproperty
    def product():
        pass
        

    @abstractmethod
    def one_mounth():
        pass


class Prop_of_Farm(metaclass = ABCMeta):    # Асбтрактный класс свойств ферм

    @abstractmethod
    def one_mounth():
        pass

    @abstractmethod
    def free_information():
        pass
    

class Animal:
 
    def __init__(self, year=0, foot=4, name=None, mammals=True, bird=False):

        self.year = year
        self.foot = foot
        self.name = name
            
        if year < 0:
            print ("Ошибка возраста")
        elif foot < 0:
            print ("Ошибка количества конечностей")

    def __getattr__(self, attr):    # Добавляем аргумент со значением 0, если пользователь обратился к несуществующему аргументу
        print ("Вы обратились к несуществующему аргументу и\
 добавили новый аргумент", attr, "со значением 0")
        return 0

    def __setattr__(self, attr, value):    # Устанавливаем значение атрибута, или изменяем значение существующего и выводим информацию об этом
        print ("Вы изменили значение атрибута", attr, "на", value)
        self.__dict__[attr] = value
        

    
            
    def song(self, sound, sound_number):    
        print (self.name, "сказал", sound, sound_number, "раз")
        
    def run(self, speed, time):    
        dist = speed*(time/60)
        return dist

    def produce (self, product, product_amount):   
        print (self.name, "произведено", product_amount, product)
        

class Duck(Prop_of_Anim, Animal):    # Наследуемся от абстрактного класса Prop_of_Anim и обычного класса Animal

    foot = 2
    mammals = False
    bird = True
    sound = 'Кря'
    speed = 10
    
    @property    # Устанавливаем свойство product со значением "Яйца" для утки
    def product(self):
        return "Яйца"

    def __repr__(self):    # Переопределяем встроенную функцию __repr__
        return "Класс уток, производящих яйца"    

    def __str__(self):    # Переопределяем встроенную функцию __str__
        return "Класс уток, производящих яйца"


        
    def one_mounth(self):
        self.product_amount = randint(10,30)
        self.sound_number = randint(100,1000)
        self.running = self.run(randint(5,15),randint (30, 50))
        self.death = randint (1,1000)

class Cow(Prop_of_Anim, Animal):

    sound = 'Му'
    speed = 20
    product = 'Молоко'
    
    def __repr__(self):
        return "Класс коров, производящих молоко"

    def __str__(self):
        return "Класс коров, производящих молоко"
 
    def one_mounth(self):
        self.product_amount = randint(300,1000)
        self.sound_number = randint(500,600)
        self.running = self.run(randint(15,25),randint (100, 200))
        self.death = randint (1,1000)

class Dog(Prop_of_Anim, Animal):

    sound = 'Гав'
    speed = 30
    product = None

    def __repr__(self):
        return "Класс собак"

    def __str__(self):
        return "Класс собак"
    
    def one_mounth(self):
        self.sound_number = randint(1000,10000000)
        self.running = self.run(randint(25,35),randint (100, 500))
        self.death = randint (1,1000)


class Farm:    
    
    def __init__(self, ducks, cows, dogs):    

        self.ducks_lst = []     
        for i in range(1,ducks+1):
            self.ducks_lst.append(Duck(year=randint(1,10), name="duck"+str(i)))    # Обращаемся из класса Farm к другому классу Duck и с ним работаем   
                
        self.cows_lst = []
        for i in range(1,cows+1):
            self.cows_lst.append(Cow(year=randint(1,30), name="cow"+str(i)))
            
        self.dogs_lst = []
        for i in range(1, dogs+1):
            self.dogs_lst.append(Dog(year=randint(1,20), name="dog"+str(i)))


    def one_mounth(self):    
        for duck in self.ducks_lst:
            duck.one_mounth()
        for cow in self.cows_lst:
            cow.one_mounth()
        for dog in self.dogs_lst:
            dog.one_mounth()

    def free_information(self):   
       
        milk_count, mu_count, cow_run = 0, 0, 0  
        death_cow = []

        for c in self.cows_lst:
            if c.death == 666:
                death_cow.append(c.name)
                del c
            else:
                milk_count += c.product_amount
                mu_count += c.sound_number
                cow_run += c.running
        if len(death_cow)>0:
            print ("Коровы", ','.join(death_cow), "умерли=(")
        print ("Коровы произвели", milk_count, "литров молока, промычали", mu_count, "раз и прошли", round(cow_run), "км")

        
        egg_count, kria_count, duck_run = 0, 0, 0   
        death_duck = []

        for c in self.ducks_lst:
            if c.death == 666:
                death_duck.append(c.name)
                del c
            else:
                egg_count += c.product_amount
                kria_count += c.sound_number
                duck_run += c.running
        if len (death_duck)>0:
            print ("Утки", ','.join(death_duck), "умерли=(")
        print ("Утки произвели", egg_count, "яиц, крянули", kria_count, "раз и прошли", round(duck_run), "км")

        
        gav_count, dog_run = 0, 0   
        death_dog = []

        for c in self.dogs_lst:
            if c.death == 666:
                death_dog.append(c.name)
                del c
            else:
                gav_count += c.sound_number
                dog_run += c.running
        if len(death_dog)>0:
            print ("Собаки", ','.join(death_dog), "умерли=(")
        print ("Собаки погавкали", gav_count, "раз и прошли", round(dog_run), "км")
       
#farm1 = Farm(2000,3000,4000)
#farm1.one_mounth()
#farm1.free_information()


d = Duck(year=6, foot=2, name='Fortuna')     # Создаем объект класса Duck с атрибутами year, foot, name
print (d)    # Выводим на экран новое представление класса
d.fly    # Пытаемся обратиться к несуществующему аргументу, присваиваем значение 0
print (d.fly)
d.fly = 200    # Изменяем значение атрибута fly
print (d.product) # Обращаемся к атрибуту product, который задекорирован property

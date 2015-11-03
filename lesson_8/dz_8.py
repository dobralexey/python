#coding: utf-8

from random import randint

class Animal:
 
    def __init__(self, year=0, foot=4, name=None, mammals=True, bird=False):

        self.year = year
        self.foot = foot
        self.name = name
            
        if year < 0:
            print ("Ошибка возраста")
        elif foot < 0:
            print ("Ошибка количества конечностей")
            
    def song(self, sound, sound_number):     # Команда "Голос", сколько раз за день
        print (self.name, "сказал", sound, sound_number, "раз")
        
    def run(self, speed, time):    # Скорость бега (км/ч) и время (мин)
        dist = speed*(time/60)
        return dist

    def produce (self, product, product_amount):    # Производить продукт со скоростью в день, выводит сколько было произведено за день
        print (self.name, "произведено", product_amount, product)
        

class Duck(Animal):
    
    foot = 2
    mammals = False
    bird = True
    sound = 'Кря'
    speed = 10
    product = 'Яйца'
    
    def one_mounth(self):
        self.product_amount = randint(10,30)
        self.sound_number = randint(100,1000)
        self.running = self.run(randint(5,15),randint (30, 50))
        self.death = randint (1,1000)

class Cow(Animal):

    sound = 'Му'
    speed = 20
    product = 'Молоко'
 
    def one_mounth(self):
        self.product_amount = randint(300,1000)
        self.sound_number = randint(500,600)
        self.running = self.run(randint(15,25),randint (100, 200))
        self.death = randint (1,1000)

class Dog(Animal):

    sound = 'Гав'
    speed = 30
    
    def one_mounth(self):
        self.sound_number = randint(1000,10000000)
        self.running = self.run(randint(25,35),randint (100, 500))
        self.death = randint (1,1000)


class Farm:    
    
    def __init__(self, ducks, cows, dogs):    # Вводим количество уток, коров и собак

        self.ducks_lst = []      # Создаем список экземпляров классов: Duck, Cow, Dog
        for i in range(1,ducks+1):
            self.ducks_lst.append(Duck(year=randint(1,10), name="duck"+str(i)))   
                
        self.cows_lst = []
        for i in range(1,cows+1):
            self.cows_lst.append(Cow(year=randint(1,30), name="cow"+str(i)))
            
        self.dogs_lst = []
        for i in range(1, dogs+1):
            self.dogs_lst.append(Dog(year=randint(1,20), name="dog"+str(i)))


    def one_mounth(self):    # Метод one_mounth проходит циклом по методам one_mounth каждого экземпляра классов
        for duck in self.ducks_lst:
            duck.one_mounth()
        for cow in self.cows_lst:
            cow.one_mounth()
        for dog in self.dogs_lst:
            dog.one_mounth()

    def free_information(self):    # Метод выводит пользователю информацию о потерянных животных, количестве продуктов, звуков и пройденном расстоянии
       
        milk_count, mu_count, cow_run = 0, 0, 0  # Для коров
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

        
        egg_count, kria_count, duck_run = 0, 0, 0    # Для уток
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

        
        gav_count, dog_run = 0, 0    # Для собак
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

        
farm1 = Farm(2000,3000,4000)
farm1.one_mounth()
farm1.free_information()



    

    
    

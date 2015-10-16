# coding: utf-8
stud_lst = ['Петя','Федор', 'Вячеслав', 'Егор', 'Егор', 'Гриша', 'Вася', 'Петя', 'Роман', 'Егор']
s = int(input('Введите ваш номер индекса:'))
print (stud_lst[s])
s1 = input ('Введите начало и конец среза:')
s2 = s1.split(':')
print (stud_lst[int(s2[0]):int(s2[1])])
counter = 0
for i in stud_lst:
    if 'р' in i:
        counter = counter + 1
    elif 'Р' in i:
        counter = counter + 1
print ('Число студентов с бувой "р" равно %d' % counter)

name_lst = []
for i in stud_lst:
    if i not in name_lst and(stud_lst.count(i)) > 1:
       name_lst.append(i)

equal_lst = [0]*len(name_lst)

for i,a in enumerate (name_lst):
    equal_lst[i] = [a]*stud_lst.count(a)
    
print ("Спиоки студентов с одинаковыми именами:",equal_lst)

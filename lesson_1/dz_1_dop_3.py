# coding: utf -8
a = float(input ("Введите первое число: "))
b = float(input ("Введите второе число: "))
c = input ("Введите действие в виде *, /, +, -: ")

if c == "*":
    res = a*b
elif c == "/":
    res = a/b
elif c == "+":
    res = a + b
elif c == "-":
    res = a - b
else:
    print ('Вы ошиблись в написании символа действия')
print (res)

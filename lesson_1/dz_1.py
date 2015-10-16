import os
prog_list = os.listdir('.')
summa = 0
f = open ('result.txt', 'w')
for i in prog_list:
    f2 = open(i)
    s = f2.read()
    if 'python' in s:
        print (i)
        f.write(i + '\n')
    counter = s.count('python')
    summa = summa + counter
print (summa)
f.write (str(summa))
f.close()

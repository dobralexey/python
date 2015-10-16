a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]
for i,j in zip(a,b):
    if abs(i - j) < 15:
        print ("Congratulations!")
    if i < j:
        print (i)
    elif i == j:
         continue
    else:
        print (j)  

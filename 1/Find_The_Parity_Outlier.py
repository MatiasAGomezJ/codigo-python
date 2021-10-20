from os import system
from time import sleep

def clear():
    system('clear')

def find_outlier(var):
    rango = range(len(var))
    odd = 0
    even = 0
    for i in range(3):
        if var[i] % 2 == 0:
            even += 1
    
    for a in rango:
        if even >= 2:
            if var[a] % 2 != 0:
                return var[a]
        if even < 2:
            if var[a] % 2 == 0:
                return var[a]

    

## -----
clear()

array = [48,2,4,8,6,22,48,62,8,5,0,2,6,8,4,0,2,6,6,204,86,20,406,4,8,620,4,8,620]
array = [5,5,5,5,5,8,5]
print(find_outlier(array))
sleep(5.5)
clear()
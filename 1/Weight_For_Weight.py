from os import system
from time import sleep

def clear():
    system('clear')

def sum_of_digits(string):
    rango2 = range(len(string))
    s = 0
    for j in rango2:
        s += int(string[j])
    return s
        

def order_weight(var):
    ori = []
    suma = []
    arr2d = [ori, suma]
    var = var.split()
    rango = range(len(var))
    for i in rango:
        sod = sum_of_digits(var[i])
        ori.append(var[i])
        suma.append(sod)
    sorted_arr2d = arr2d

    
    return arr2d        

## -----
clear()

string = "10 58 47 50 310 8005"
print(order_weight(string))
sleep(5.5)
clear()
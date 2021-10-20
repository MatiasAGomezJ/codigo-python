from os import system
from time import sleep

def clear():
    system('clear')

def odd_or_even(var):
    sum = 0
    for i in range(len(var)):
        sum += var[i]
    
    if sum % 2 == 0:
        return "even"
    else:
        return "odd"

## -----
clear()

array = [0,-1,8,6,-5]
print(odd_or_even(array))
sleep(5.5)
clear()
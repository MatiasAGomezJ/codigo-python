from os import system
from time import sleep

def clear():
    system('clear')

def century(year):
    cent = int(year/100)

    if year%100 != 0:    
        cent += 1

    return cent

## -----
clear()

año = 1700
siglo = century(año)

print(siglo)

sleep(5.5)
clear()
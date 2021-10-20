from os import system
from time import sleep

def clear():
    system('clear')

def fsi(arr):
    numero = -200
    for a in arr:
        if a == arr[0]:
            numero = a
        if numero > a:
            numero = a
    
    print(numero)

## -----
clear()

numeros = [5,8,3,7,9,6]

fsi(numeros)

sleep(5.5)
clear()

from os import name, system
from time import sleep

def clear():
    system('clear')

def alphabet_position(var):
    var = var.lower()
    rango = range(len(var))
    numeros_por_letras = ""
    for i in rango:
        if var[i] == "a":
            num = 1
        elif var[i] == "b":
            num = 2
        elif var[i] == "c":
            num = 3
        elif var[i] == "d":
            num = 4
        elif var[i] == "e":
            num = 5
        elif var[i] == "f":
            num = 6
        elif var[i] == "g":
            num = 7
        elif var[i] == "h":
            num = 8
        elif var[i] == "i":
            num = 9
        elif var[i] == "j":
            num = 10
        elif var[i] == "k":
            num = 11
        elif var[i] == "l":
            num = 12
        elif var[i] == "m":
            num = 13
        elif var[i] == "n":
            num = 14
        elif var[i] == "o":
            num = 15
        elif var[i] == "p":
            num = 16
        elif var[i] == "q":
            num = 17
        elif var[i] == "r":
            num = 18
        elif var[i] == "s":
            num = 19
        elif var[i] == "t":
            num = 20
        elif var[i] == "u":
            num = 21
        elif var[i] == "v":
            num = 22
        elif var[i] == "w":
            num = 23
        elif var[i] == "x":
            num = 24
        elif var[i] == "y":
            num = 25
        elif var[i] == "z":
            num = 26
        else:
            continue
        if i != 0:
            numeros_por_letras += " "
        numeros_por_letras += str(num)
    return numeros_por_letras

## -----
clear()

string = "Los ssd no son discos duros"
print(alphabet_position(string))
sleep(5.5)
clear()
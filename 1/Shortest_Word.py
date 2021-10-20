from os import system
from time import sleep

def clear():
    system('clear')

def find_short(var):
    lenvar = len(var)
    shortest = 100
    count = 0
    for c in var:
        if c == ' ':
            if count < shortest:
                shortest = count
            count = 0
            continue
        count += 1
    if count < shortest:
        shortest = count
    return shortest


## -----
clear()

string = "Muchas cosas seguidas, una de estas palabras es la mas corta de todas a"
print(find_short(string))
sleep(5.5)
clear()
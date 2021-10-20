from os import system, terminal_size
from time import sleep

def clear():
    system('clear')

def columnize(items, columns_count):
    leni = len(items)
    rango = range(leni)
    length = len(items[-1])
    text = ""
    for i in rango:
        if len(items[i]) < length:
            l = length - len(items[i])
            for j in range(l):
                items[i] += ' '
    
    for a in rango:
        text += items[a]
        if a+1 == leni:
            break
        if (a+1) % columns_count == 0:
            text += "\n"
        if (a-1) % columns_count != 0:
            text += "| "
    return text

## -----
clear()

items = ["0", "01", "012", "0123", "01234", "012345"]
columns_count = 4
print(columnize(items, columns_count))
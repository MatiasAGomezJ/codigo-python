from os import system
from time import sleep

def clear():
    system('clear')

def expanded_form(var):
    lenvar = len(str(var))
    lenvarr = range(len(str(var)))
    nums = []
    phrase = ""
    for a in lenvarr:
        if var == 0:
            break
        zero = var%10
        var -= zero
        var = var//10
        nums.append(int(zero))

    for n in lenvarr:
        pos = lenvar-n-1
        r = nums[pos]*10**pos
        if r == 0:
            continue
        if n != 0:
            phrase += " + "
        phrase += str(r)
    return phrase

## -----

clear()

numero = 704030
print(expanded_form(numero))

sleep(5.5)
clear()
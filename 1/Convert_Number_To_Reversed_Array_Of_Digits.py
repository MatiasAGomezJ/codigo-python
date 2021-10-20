from os import system
from time import sleep

def clear():
    system('clear')

def digitize(n):
    lenn = range(len(str(n)))
    zero = None
    oremun = []
    for a in lenn:
        if n == 0:
            break
        zero = n%10
        n -= zero
        n = n//10
        oremun.append(int(zero))
    return oremun

## -----
clear()

numero = 95513774773429578
print(digitize(numero))

sleep(10)
clear()
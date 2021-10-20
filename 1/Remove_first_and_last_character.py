from os import system
from time import sleep

def clear():
    system('clear')

def remove_char(s):
    s2 = ""
    lens = len(s)
    for c in range(lens):
        if c == lens-1:
            break
        if c == 0:
            continue
        s2 += s[c]
    return s2

## -----
clear()

trin = remove_char("Olafsinojo")
print(trin)

sleep(5.5)
clear()
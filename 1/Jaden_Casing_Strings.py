from os import system
from time import sleep
import string

def clear():
    system('clear')

def to_jaden_case(var):
    return string.capwords(var)

## -----
clear()

frase = "Habia una vez un circo con un elegante y un mono"
print(to_jaden_case(frase))
sleep(5.5)
clear()
from os import system
from time import sleep
import math
def clear():
    system('clear')

def find_next_square(var):
    # Return the next square if sq is a square, -1 otherwise
    base = math.sqrt(var)
    if base % 1 != 0:
        return -1
    base += 1
    var2 = int(base**2)
    return var2

## -----
clear()

numero = 144
print(find_next_square(numero))
sleep(5.5)
clear()
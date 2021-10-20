from os import system
from time import sleep

def clear():
    system('clear')

def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce >= 1 or bounce <= 0 or window >= h:
        return -1 
    veces_visto = 1
    while True:
        h *= bounce
        if h > window:
            veces_visto += 2
        else:
            break
    return veces_visto

## -----
clear()

altura = 5
rebote = 0.5
ventana = 2
print(bouncing_ball(altura, rebote, ventana))
sleep(5.5)
clear()
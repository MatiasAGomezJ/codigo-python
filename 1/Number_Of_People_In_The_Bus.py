from os import system
from time import sleep

def clear():
    system('clear')

def number(bus_stops):
    up = 0
    down = 0
    for i in range(2):
        for j in range(len(bus_stops)):
            if i == 0:
                up += bus_stops[j][i]
            if i == 1:
                down += bus_stops[j][i]
    total = up - down
    return total
    
    

## -----
clear()

bus_stops = [[10,0],[3,5],[5,8]]
print(number(bus_stops))
sleep(5.5)
from os import system
system('clear')

from Animal import *

def main2():
    
    animal1 = Animal(2)
    print(animal1.get_variable())
    animal1.set_variable(6)
    print(animal1.get_variable())

main2()
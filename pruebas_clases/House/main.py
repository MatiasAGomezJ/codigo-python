from os import system

from House import House
system('clear')

def main():
    sep = '-' * 29

    # -------------------------------------------------------------------

    house1 = House("cartrofa", 16, 2, True)
    house2 = House("halfonso", 5461, 67845, False)

    neighborhood = []

    neighborhood.append(house1)
    neighborhood.append(house2)

    for house in neighborhood:
        print(house.get_existence())
        print(house.get_name())
        print(house.get_windows())
        print(house.get_doors())
        print(house.get_has_garage())

        if neighborhood.index(house) != len(neighborhood) - 1: print(sep)

    print(sep) # -------------------------------------------------------------------

    house3 = House("jesus cristo", 6, 6, True)
    house4 = House("atundero", 800, 100, False)

    neighborhood = []

    neighborhood.append(house3)
    neighborhood.append(house4)

    for house in neighborhood:
        house.print_basic_information()

        if neighborhood.index(house) != len(neighborhood) - 1:
            print(sep)

    print(sep) # -------------------------------------------------------------------

    print(house1.get_windows())
    house1.set_windows(18)
    print(house1.get_windows())

main()
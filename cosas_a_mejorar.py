
class Yatzy:
    ONE, TWO, THREE, FOUR, FIVE, SIX = 1, 2, 3, 4, 5, 6

    @staticmethod
    def oneList(d1, d2, d3, d4, d5): # Nombres de la funcion, nombre de las variables
        diceList = [d1, d2, d3, d4, d5]
        return diceList

    @staticmethod
    def chance(diceList):
        points = 0
        for dice in diceList:
            points += dice
        return points

    @staticmethod
    def yatzy(diceList):
        if diceList.count(diceList[0]) != Yatzy.FIVE:
            return 0
        return 50

    @staticmethod
    def ones(diceList):
        points = 0
        for dice in diceList:
            if dice == Yatzy.ONE:
                points += Yatzy.ONE
        return points
    
    @staticmethod
    def twos(diceList):
        points = 0
        for dice in diceList:
            if dice == Yatzy.TWO:
                points += Yatzy.TWO
        return points
    
    @staticmethod
    def threes(diceList):
        points = 0
        for dice in diceList:
            if dice == Yatzy.THREE:
                points += Yatzy.THREE
        return points
    
    @staticmethod
    def fours(diceList):
        points = 0
        for dice in diceList:
            if dice == Yatzy.FOUR:
                points += Yatzy.FOUR
        return points
    
    @staticmethod
    def fives(diceList):
        points = 0
        for dice in diceList:
            if dice == Yatzy.FIVE:
                points += Yatzy.FIVE
        return points
    
    @staticmethod
    def sixes(diceList):
        points = 0
        for dice in diceList:
            if dice == Yatzy.SIX:
                points += Yatzy.SIX
        return points

    @staticmethod
    def score_pair(diceList):
        for num in range(6,0,-1):
            if diceList.count(num) >= Yatzy.TWO:
                return num * Yatzy.TWO  # Utilizar solo un return guardando el valor en...
        return 0                        # ... una variable haciendo return de esta varible
            
    @staticmethod
    def two_pair(diceList):
        points = 0
        counter = 0 # Cambiar nombre. EJ: amount_pairs
        for num in range(6,0,-1):
            if diceList.count(num) >= Yatzy.TWO:
                points += num * Yatzy.TWO
                counter += Yatzy.ONE
            elif counter == Yatzy.TWO: 
                return points           
                # ??Hace falta un else o cambiar el 'elif' por un 'if'?
        return 0
    
    @staticmethod
    def three_of_a_kind(diceList):
        for dice in diceList:
            if diceList.count(dice) >= Yatzy.THREE:
                return(dice * Yatzy.THREE)  # Quitar parentesis
        return 0
    
    @staticmethod
    def four_of_a_kind(diceList):
        # El metodo no funciona correctamente, no contempla todas las combinaciones de numeros
        for dice in diceList:
            if diceList.count(diceList[0]) < Yatzy.FOUR and diceList.count(diceList[1]) < Yatzy.FOUR:
                return 0
            else:
                return(dice * Yatzy.FOUR)            

    import collections
    @staticmethod
    def smallStraight(diceList):
        if Yatzy.collections.Counter(diceList) == Yatzy.collections.Counter(range(1,6)):
            return 15   # 15 es un numero magico, en este caso es la suma de los numeros que aparecen en la lista
        return 0

    @staticmethod
    def largeStraight(diceList):
        if Yatzy.collections.Counter(diceList) == Yatzy.collections.Counter(range(2,7)):
            return 20   # 20 es un numero magico, en este caso es la suma de los numeros que aparecen en la lista
        return 0
    
    @staticmethod
    def fullHouse(diceList):# A mejorar
        flag = False    # Cambiar nombre
        for dice in diceList:
            if diceList.count(dice) == Yatzy.THREE: # Igual el uso de un while es mejor
                flag = True
                break
        for otherDice in diceList:
            if flag and diceList.count(otherDice) == Yatzy.TWO:
                    return (dice * Yatzy.THREE + otherDice * Yatzy.TWO)
        return 0

        
import math
from square_generator import *


class CubicGenerator(SquareGenerator):
    def getSquaresForRange(start, end):
        if start > end:
            print('Start cant be bigger then end')
            return
        else:
            return [(n ** 3) for n in range(start, end + 1)]

def getSquaresRange(start, end):
    return [(n ** 2) for n in range(start, end + 1)]


squaresList = [(n ** 2) for n in range(1, 11)]

print(squaresList)
print(SquareGenerator.getSquaresForRange(1,10))
print(SquareGenerator.getSquareRootsFromList(squaresList))
print(CubicGenerator.getSquaresForRange(1,10))





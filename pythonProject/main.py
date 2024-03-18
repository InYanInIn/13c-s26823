import math
from square_generator import *


class CubicGenerator(SquareGenerator):
    def getCubesForRange(start, end):
        if start > end:
            print('Start cant be bigger than the end')
            return
        else:
            return [(n ** 3) for n in range(start, end + 1)]

    def getSquaresForRange(start, end):
        if start > end:
            return Exception('ERROR: Start cant be bigger than the end!')
        else:
            return [(n ** 3) for n in range(start, end + 1)]

def getSquaresRange(start, end):
    return [(n ** 2) for n in range(start, end + 1)]


squaresList = [(n ** 2) for n in range(1, 11)]

print(squaresList)
print(SquareGenerator.getSquaresForRange(1,10))
print(SquareGenerator.getSquaresForRange(10,1))
print(SquareGenerator.getSquareRootsFromList(squaresList))
print(CubicGenerator.getCubesForRange(1,10))
print(CubicGenerator.getSquaresForRange(100,10))





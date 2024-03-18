import math


class SquareGenerator:
    def getSquaresForRange(start, end):
        if start > end:
            print('Start cant be bigger then end')
            return
        else:
            return [(n ** 2) for n in range(start, end + 1)]

    def getSquareRootsFromList(list):
        return [math.sqrt(n) for n in list]
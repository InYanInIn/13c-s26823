squaresList = [(n ** 2) for n in range(1, 11)]
print(squaresList)

def getSquaresRange(start, end):
    return [(n ** 2) for n in range(start, end + 1)]


class SquareGenerator:
    def getSquaresForRange(start, end):
        return [(n ** 2) for n in range(start, end + 1)]

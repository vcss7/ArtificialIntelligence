class Num:
    # holds a num and its coordinate in an n-puzzle
    # function to  swap coordinates with other nums
    # checks and keeps track if the number is in the correct coordinate

    def __init__(self, num, xCoord, yCoord):
        self.num = num
        self.x = xCoord
        self.y = yCoord
        self.sorted = false
        self.sortedX = -1
        self.sortedY = -1

    def swap(self, other):
        xTemp = self.x
        yTemp = self.y
        self.x = other.x
        self.y = other.y
        other.x = xTemp
        other.y = yTemp

    def isSorted(self):
        """ TODO """
        return false


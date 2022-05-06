import random

class graph():
    def __init__(self) :
        self.matrix = [
            [1,2,4],
            [5,0,7],
            [3,6,8]
        ]
    
    def printMatrix(self):
        for i in range(3):
            for j in range(3):
                print(self.matrix[i][j],end=' ')
            print()

    def getCost(self):
        error=0
        if self.matrix[0][0] != 1:
            error+=1
        if self.matrix[0][1] != 2:
            error+=1
        if self.matrix[0][2] != 3:
            error+=1
        if self.matrix[1][0] != 4:
            error+=1
        if self.matrix[1][1] != 5:
            error+=1
        if self.matrix[1][2] != 6:
            error+=1
        if self.matrix[2][0] != 7:
            error+=1
        if self.matrix[2][1] != 8:
            error+=1
        return error

    def canSwap(self,i,j):
        if i-1>=0 & self.matrix[i-1][j]==0:
            return True
        if i+1<=2 & self.matrix[i+1][j]==0:
            return True
        if j-1>=0 & self.matrix[i][j-1]==0:
            return True
        if j+1<=2 & self.matrix[i][j+1]==0:
            return True
        return False

    def getZero(self):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j]==0:
                    return i,j

    def swap(self):
        irand = random.randint(0,2)
        jrand = random.randint(0,2)

        if self.canSwap(irand,jrand):
            val = self.matrix[irand][jrand]
            izero, jzero = self.getZero()
            self.matrix[izero][jzero] = val
            self.matrix[irand][jrand] = 0
        else:
            self.swap() 

    def hillClimbing(self):
        cost = self.getCost()
        if cost == 0:
            print("Solution found")
            self.printMatrix()
        while True:
            self.swap()
            newCost = self.getCost()
            print(newCost)

            if newCost == 0:
                print("Solution found")
                self.printMatrix()
                return
            elif newCost<cost:
                cost = newCost

g = graph()
g.printMatrix()
g.hillClimbing()
import random


class puzzle:
    def __init__(self):
        self.matrix = [
            [1, 2, 4],
            [5, 0, 7],
            [3, 6, 8]]

    def printm(self, matrix):
        for i in range(3):
            for j in range(3):
                print(self.matrix[i][j], ' ', end='')
            print('\n')

    def CostFunction(self, matrix):
        errors = 0
        if matrix[0][0] != 1:
            errors += 1
        if matrix[0][1] != 2:
            errors += 1
        if matrix[0][2] != 3:
            errors += 1
        if matrix[1][0] != 4:
            errors += 1
        if matrix[1][1] != 5:
            errors += 1
        if matrix[1][2] != 6:
            errors += 1
        if matrix[2][0] != 7:
            errors += 1
        if matrix[2][1] != 8:
            errors += 1
        return errors

    def isNextTo(self, val):
        i = 0
        j = 0
        for _ in range(len(self.matrix)):
            for k in range(len(self.matrix)):
                if self.matrix[_][k] == val:
                    i = _
                    j = k
                    break
        print(i,j)
        if self.matrix[i-1][j] == 0 and i-1 >= 0:
            # return (i-1,j)
            return True
        if i + 1 <= 2:
            if self.matrix[i+1][j] == 0:
                return True
        if self.matrix[i][j-1] == 0 and j - 1 >= 0:
            # return (i,j-1)
            return True
        if j + 1 <= 2:
            if self.matrix[i][j+1] == 0:
                return True
        return False

    def getZeroIndex(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    return i, j

    def swap(self, matrix):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        ii, jj = self.getZeroIndex()
        print(i,j)

        if (self.isNextTo(self.matrix[i][j])):
            matrix[i][j], matrix[ii][jj] = matrix[ii][jj], matrix[i][j]
            return matrix
        else:
            # print(self.printm(self.matrix))
            return self.swap(matrix)

    def HillClimbing(self, matrix):
        score = self.CostFunction(matrix)

        if score <= 0:
            print("Found!")
            self.printm(matrix)
            return matrix

        while score >= 0:
            actual = matrix
            # print(matrix)
            self.swap(actual)
            new_score = self.CostFunction(actual)

            if new_score <= 0:
                print("Found!")
                print("--------")
                self.printm(actual)
                return actual
            elif new_score < score:
                score = new_score


mat = puzzle()
print(mat.printm(mat.matrix))
mat.HillClimbing(mat.matrix)
print("--------")

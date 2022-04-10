finalState = {
    (0,0):1,
    (0,1):2,
    (0,2):3,
    (1,0):4,
    (1,1):5,
    (1,2):6,
    (2,0):7,
    (2,1):8,
    (2,2):0
}

visited = {}

testVar = 0 

class puzzle:
     
    # parameterized constructor
    def __init__(self, matrix, startI, startJ, level):
        self.matrix = matrix
        self.totalDistance = calculateTotalDistance(matrix=matrix)
        self.startI = startI
        self.startJ = startJ
        self.level = level
        self.flag = calculateFlag(self.totalDistance,self.level)

def individualDistance(nodeValue, i, j):
    if finalState[(i,j)] == nodeValue:
        return 0
    else: 
        return 1

def calculateTotalDistance(matrix):
    distance = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                continue
            else:
                distance+=individualDistance(matrix[i][j], i, j)
    return distance

def calculateFlag(distance, level):
    return distance+level

def moveLeft(puzzleReceived):    
    leftMatrix = []
    for i in range(3):
        leftMatrix.append(puzzleReceived.matrix[i][:])
    startI = puzzleReceived.startI
    startJ = puzzleReceived.startJ

    if (startI,startJ) in visited.keys():
        if "L" in visited[(startI,startJ)] :
            return None

    if startJ==0:
        return None

    leftMatrix[startI][startJ] = leftMatrix[startI][startJ-1]
    leftMatrix[startI][startJ-1] = 0
    puzzleToBeReturned = puzzle(matrix=leftMatrix, startI=startI, startJ=startJ-1, level=puzzleReceived.level+1)
    return puzzleToBeReturned

def moveRight(puzzleReceived):
    
    rightMatrix = []
    for i in range(3):
        rightMatrix.append(puzzleReceived.matrix[i][:])
    # print("right ( ",startI,", ",startJ,")")
    startI = puzzleReceived.startI
    startJ = puzzleReceived.startJ

    if (startI,startJ) in visited.keys():
        if "R" in visited[(startI,startJ)] :
            return None

    if startJ==2:
        return None

    rightMatrix[startI][startJ] = rightMatrix[startI][startJ+1]
    rightMatrix[startI][startJ+1] = 0
    puzzleToBeReturned = puzzle(matrix=rightMatrix, startI=startI, startJ=startJ+1, level=puzzleReceived.level+1)
    return puzzleToBeReturned

def moveUp(puzzleReceived):
    
    upMatrix = []
    for i in range(3):
        upMatrix.append(puzzleReceived.matrix[i][:])
    startI = puzzleReceived.startI
    startJ = puzzleReceived.startJ

    if (startI,startJ) in visited.keys():
        if "U" in visited[(startI,startJ)] :
            return None

    if startI==0:
        return None
    # print("up ( ",startI,", ",startJ,")")
    upMatrix[startI][startJ] = upMatrix[startI-1][startJ]
    upMatrix[startI-1][startJ] = 0
    puzzleToBeReturned = puzzle(matrix=upMatrix, startI=startI-1, startJ=startJ, level=puzzleReceived.level+1)
    return puzzleToBeReturned

def moveDown(puzzleReceived):
    
    downMatrix = []
    for i in range(3):
        downMatrix.append(puzzleReceived.matrix[i][:])
    startI = puzzleReceived.startI
    startJ = puzzleReceived.startJ

    if (startI,startJ) in visited.keys():
        if "D" in visited[(startI,startJ)] :
            return None

    if startI==2:
        return None
    # print("down ( ",startI,", ",startJ,")")
    downMatrix[startI][startJ] = downMatrix[startI+1][startJ]
    downMatrix[startI+1][startJ] = 0
    puzzleToBeReturned = puzzle(matrix=downMatrix, startI=startI+1, startJ=startJ, level=puzzleReceived.level+1)
    return puzzleToBeReturned

def printMatrix(matrix):
    for i in range(3):
        # for j in range(3):
        print(matrix[i])

def findMinFlag(minFlag, newFlag):
    if newFlag.flag < minFlag.flag:
        return newFlag
    return minFlag
        
def solvePuzzle(puzzleReceived):

    if puzzleReceived.totalDistance == 0:
        print("Solution found!!!!")
        printMatrix(puzzleReceived.matrix)
        return

    print("original : ",puzzleReceived.flag," originalLevel : ",puzzleReceived.level)
    # printMatrix(puzzleReceived.matrix)

    rightFlag = moveRight(puzzleReceived=puzzleReceived)
    if rightFlag!=None:
        print("right : ",rightFlag.flag)
        # printMatrix(rightFlag.matrix)

    
    minFlag = rightFlag

    leftFlag = moveLeft(puzzleReceived=puzzleReceived)
    if leftFlag!=None:
        print("leftFlag : ",leftFlag.flag," leftLevel : ",leftFlag.level)
        # printMatrix(leftFlag.matrix)
        
        if minFlag:
            minFlag = findMinFlag(minFlag, leftFlag)
        else:
            minFlag = leftFlag
        # print("original : ",puzzleReceived.flag," originalLevel : ",puzzleReceived.level)
        # printMatrix(puzzleReceived.matrix)


    downFlag = moveDown(puzzleReceived=puzzleReceived)
    if downFlag != None:
        print("down : ",downFlag.flag)
        # printMatrix(downFlag.matrix)
        if minFlag:
            minFlag = findMinFlag(minFlag, downFlag)
        else:
            minFlag = downFlag

    upFlag = moveUp(puzzleReceived=puzzleReceived)
    if upFlag != None:
        print("up : ",upFlag.flag)
        # printMatrix(upFlag.matrix)
        if minFlag:
            minFlag = findMinFlag(minFlag, upFlag)
        else:
            minFlag = upFlag        
                

    if minFlag==None:
        print("----NO SOLUTION POSSIBLE-----")
        return

    # findMin(rightFlag.flag, leftFlag.flag, upFlag.flag, downFlag.flag)
    print("Final : ",minFlag.flag)
    printMatrix(minFlag.matrix)

    if puzzleReceived.startI > minFlag.startI:
        nodeVisited = "U"
        opposite = "D"
    elif puzzleReceived.startI < minFlag.startI:
        nodeVisited = "D"
        opposite = "U"
    elif puzzleReceived.startJ > minFlag.startJ:
        nodeVisited = "L"
        opposite = "R"
    elif puzzleReceived.startJ < minFlag.startJ:
        nodeVisited = "R"
        opposite = "D"

    if (puzzleReceived.startI, puzzleReceived.startJ) not in visited.keys():
        visited[(puzzleReceived.startI, puzzleReceived.startJ)] = []
    if (minFlag.startI, minFlag.startJ) not in visited.keys():
        visited[(minFlag.startI, minFlag.startJ)] = []
    visited[(puzzleReceived.startI, puzzleReceived.startJ)].append(nodeVisited)
    # visited[(minFlag.startI, minFlag.startJ)].append(opposite)


    
    
    print(visited)
    # if minFlag.level==3:
    #     return
    solvePuzzle(minFlag)

    

    return

print("Enter the 3x3 matrix")
matrix = []

for i in range(3):
    # print("Row number ",i)
    l = []
    for j in range(3):
        a = int(input())
        if a == 0:
            startI = i
            startJ = j        
        # nodeToBeEntered = node(i,j,a)
        if (a<0) or (a>8) :
            print("Enter the number correctly(0-8)")
            break
        l.append(a)
    matrix.append(l)

initial = puzzle(matrix=matrix, startI=startI, startJ=startJ, level=0)
testVar = 0
solvePuzzle(initial)

# 1
# 2
# 3
# 0
# 4
# 6
# 7
# 5
# 8

   
# print(matrix[startI][startJ])
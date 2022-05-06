import random

class VaccumCleaner:

    def __init__(self, side, garbagePresentLeft, garbagePresentRight):
        self.side = side
        self.garbagePresentLeft = garbagePresentLeft
        self.garbagePresentRight = garbagePresentRight
    
    def compare(self,goal):
        if self.side == goal.side and self.garbagePresentLeft == goal.garbagePresentLeft and self.garbagePresentRight == goal.garbagePresentRight:
            return True
        return False

goalState = VaccumCleaner("left",False,False)

currentState = VaccumCleaner("right",False,False)

actions = {"left","right","suck"}

path = []

def isGarbage():
    return bool(random.getrandbits(1))

def action(currentSide):
    return random.sample(actions-{currentSide},1)[0]

def conditionalPlan():
    print("Position\t"+"Dirt on left\t"+"Dirt on right\t"+"Action\n")
    while not currentState.compare(goalState):
        newAction = action(currentState.side)
        print(currentState.side+"\t\t"+str(currentState.garbagePresentLeft)+"\t\t"+str(currentState.garbagePresentRight)+"\t\t"+newAction+"\n")
        if newAction!="suck":
            if currentState.side == "right" and currentState.garbagePresentRight!=True:
                currentState.garbagePresentRight = isGarbage()
            elif currentState.side == "left" and currentState.garbagePresentLeft!=True:
                currentState.garbagePresentLeft = isGarbage()
            currentState.side = newAction
        else:
            if currentState.side == "right":
                currentState.garbagePresentRight = isGarbage()
            elif currentState.side == "left":
                currentState.garbagePresentLeft = isGarbage()
        path.append(newAction)
    print(currentState.side+"\t\t"+str(currentState.garbagePresentLeft)+"\t\t"+str(currentState.garbagePresentRight)+"\t\t"+newAction+"\n")

conditionalPlan()
print("Final Path : ")
print(path)
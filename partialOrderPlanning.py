import random

class Action:
    def __init__(self, name):
        self.name = name
        self.preconditions = []
        self.effects = []

    def addPreconditions(self, conditions):
        for condition in conditions:
            self.preconditions.append(condition)
    def addEffects(self,effects):
        for effect in effects:
            self.effects.append(effect)

def getNextAction():
    return random.sample(set(actions)-set(sequenceOfActions),1)[0]

def check(conditions):
    for condition in conditions:
        if condition not in sequenceOfActions:
            return False
    return True

def printSequenceOfActions():
    for action in sequenceOfActions:
        # print(type(action))
        if type(action)!=str:
            print(action.name,end=" ")
        else:
            print(action,end=" ")
    print("\n")

def partialOrderPlanning():
    while True:
        nextAction = getNextAction() 
        if check(nextAction.preconditions):
            sequenceOfActions.append(nextAction)
            for effect in nextAction.effects:
                sequenceOfActions.append(effect)
            printSequenceOfActions()
        if sequenceOfActions[-1] == Finish:
            break

Start = Action("Start")
RightSock = Action("RightSock")
LeftSock = Action("LeftSock")
RightShoe = Action("RightShoe")
LeftShoe = Action("LeftShoe")
Finish = Action("Finish")

actions = [Start,RightSock,LeftSock,RightShoe,LeftShoe,Finish]

RightShoe.addPreconditions([RightSock])
LeftShoe.addPreconditions([LeftSock])
Finish.addPreconditions([RightShoe,LeftShoe])

RightSock.addEffects(["RightSockOn"])
LeftSock.addEffects(["LeftSockOn"])
RightShoe.addEffects(["RightShoeOn"])
LeftShoe.addEffects(["LeftShoeOn"])

sequenceOfActions = []

sequenceOfActions.append(actions[0])
for action in actions:
    print("ACTION : ",end=" ")
    print(action.name,end=" ")
    print("\nPRECONDITIONS : ",end=" ")
    for precondition in action.preconditions:
        print(precondition.name,end=" ")
    print("\nEFFECTS : ",end=" ")
    print(action.effects)
    print("\n")

partialOrderPlanning()
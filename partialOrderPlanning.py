import json
import random
actions = {
            "1":"Start",
            "2":"RightSock",
            "3":"RightSockOn",
            "4":"LeftSock",
            "5":"LeftSockOn",
            "6":"RightShoe",
            "7":"RightShoeOn",
            "8":"LeftShoe",
            "9":"LeftShoeOn",
            "10":"Finish"
            }
preConditions = {}
sequenceOfActions = []

def getNextAction():
    return random.sample(set(actions.values())-set(sequenceOfActions),1)[0]

def check(conditions):
    for condition in conditions:
        if condition not in sequenceOfActions:
            return False
    return True

for i in range(1,len(actions)+1):
    print(actions)
    choice = 0
    print("Enter the precondtions for : "+actions[str(i)])
    choice = int(input())
    while choice!=-1:
        if actions[str(i)] not in preConditions.keys():
            preConditions[actions[str(i)]] = []
        preConditions[actions[str(i)]].append(actions[str(choice)])
        choice = int(input())

sequenceOfActions.append(actions["1"])
print("PRECONDITIONS : ")
print(json.dumps(preConditions,indent=3))
while True:
    nextAction = getNextAction() 
    if nextAction in preConditions.keys():
        if check(preConditions[nextAction]):
            sequenceOfActions.append(nextAction)
            print(sequenceOfActions)
    else:
        sequenceOfActions.append(nextAction)
        print(sequenceOfActions)
    if sequenceOfActions[-1] == "Finish":
        break


print(sequenceOfActions)

# -1
# -1
# 2
# -1
# -1
# 4
# -1
# 2
# 3
# -1
# 6
# -1
# 5
# 6
# -1
# 8
# -1
# 7
# 9
# -1
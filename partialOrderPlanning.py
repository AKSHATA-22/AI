actions = {
            "1":"Start",
            "2":"RightSock",
            "3":"RightSockOn",
            "4":"LeftSock",
            "5":"LeftSockOn",
            "6":"RightShoe",
            "7":"RightShoeOn",
            "8":"LeftShoe",
            "9":"LeftSoeOn",
            "10":"Finish"
            }
preConditions = {}

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

print(preConditions)


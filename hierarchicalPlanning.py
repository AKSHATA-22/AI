# Applying Hierarchical Planning in going from one place to another.

print("Travelling from source to destination (1. Bus, 2. Train, 3. Car)")
actions = ["Select destination"]
options1 = [
           {
                "action":"Go by bus"
           },
           {
                "action":"Go by train"
           },
           {
                "action":"Go by car"
           }
]
options2 = [
            {
                "action":"Book tickets"
           },
           {
                "action":"Board from stop"
           },
]
carOptions = [
              {
                  "action":"Fill fuel",
              }
]
options3 = [
            {
                "action":"Start your travel",
            },
            {
                "action":"Drive to destination"
            },

]

var1 = int(input("Select either 1,2,3: "))
if var1==1:
  actions.append(options1[0]["action"])
  var2 = int(input("Select either 1. Book tickets, 2. Board from stop:: "))
  if var2==1:
    actions.append(options2[0]["action"])
  if var2==2:
    actions.append(options2[1]["action"])
    actions.append(options3[0]["action"])
  pass

if var1==2:
  actions.append(options1[1]["action"])
  var2 = int(input("Select either 1. Book tickets, 2. Board from stop: "))
  if var2==1:
    actions.append(options2[0]["action"])
    actions.append(options3[0]["action"])
  if var2==2:
    actions.append(options2[1]["action"])
  pass

if var1==3:
  actions.append(options1[2]["action"])
  actions.append(carOptions[0]["action"])
  actions.append(options3[1]["action"])
  pass

actions.append("Reach destination")
print("Actions: ",actions)
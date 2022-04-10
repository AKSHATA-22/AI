class Graph:

    def __init__(self,n):
        self.nodes = {}
        for i in range(n):
            self.nodes[i] = {}
            self.nodes[i]["neighbours"] = {}
    
    def addNode(self,a,b,c):
        self.nodes[a]["neighbours"][b] = c

    def addWeight(self,node,weight):
        self.nodes[node]["weight"] = weight
path = []

def findPathValue(graph):
    print("path",path)
    if(len(path)>1):
        length = 0
        for i in range(len(path)-1):
            length = graph.nodes[path[i]]["neighbours"][path[i+1]] + length
        return length
    else:
        return 0


def Astar(graph,source,destination):

    if source == destination:
        return
    else:
        min = 100
        print(source)
        pathValue = findPathValue(graph)
        for neighbour in graph.nodes[source]["neighbours"].keys():
            f =  pathValue + graph.nodes[neighbour]["weight"] + graph.nodes[source]["neighbours"][neighbour]
            print(neighbour,"-->",f)
            if f<min:
                min = f
                next = neighbour
                
        path.append(next)
        Astar(graph,next,destination)


        
n = int(input("Enter the number of nodes : "))

g = Graph(n)
print("Enter -1,-1,-1 to stop : ")
while True:
    inp = input().split(sep=",")
    a,b,c = int(inp[0]),int(inp[1]),int(inp[2])
    if a==-1 and b==-1 and c==-1:
        break
    g.addNode(a,b,c)

print("Enter the heuristic value of the nodes : ")
for i in range(n):
    g.addWeight(i,int(input()))
dest = int(input("Enter the destination : "))
path.append(0)
Astar(g,0,dest)
print(g.nodes)
print(path)

# 0,1,4
# 0,2,3
# 1,4,12
# 2,4,10
# 2,5,7
# 5,4,2
# 1,3,5
# 3,6,16
# 4,6,5
# -1,-1,-1

# 14
# 12
# 11
# 11
# 4
# 6
# 0
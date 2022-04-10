class Graph:

    def __init__(self,n):
        self.nodes = {}
        for i in range(n):
            self.nodes[i] = []
    
    def addNode(self,a,b):
        self.nodes[a].append(b)
    
def BFS(graph,start,n):
    status = [1]*n
    print("Status : ",status)
    queue = []

    status[start] = 2
    queue.append(0)
    while queue:
        element = queue.pop(0)

        print("Element : ",element)

        neighbours = graph.nodes[element]

        for neighbour in neighbours:
            if status[neighbour] == 1:
                status[neighbour] = 2
                queue.append(neighbour)
        status[element] = 3
        print("Queue : ",queue)
        print("Status : ",status)
        

n = int(input("Enter the number of nodes : "))
g = Graph(n)
print("Enter -1,-1 to stop : ")
while True:
    inp = input().split(sep=",")
    a,b = int(inp[0]),int(inp[1])
    if a==-1 and b==-1:
        break
    g.addNode(a,b)

print(g.nodes)
BFS(g,0,n)

# 0,1
# 0,2
# 0,3
# 1,4
# 2,1
# 2,6
# 3,2
# 3,6
# 4,2
# 4,5
# 5,2
# 6,5
# 7,4
# 5,7
# 6,5
# 6,7
# 6,8
# 7,8
# 8,5
# -1,-1
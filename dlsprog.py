from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DLS(self,source,target,maxDepth):

        if maxDepth <= 0 :
            return False

        if source == target:
            return True

        for neighbour in self.graph[source]:
            if (self.DLS(neighbour,target,maxDepth-1)):
                return True

        return False

    # def IDDFS(self,source,target,maxDepth):
    #     for i in range(maxDepth):
    #         if (self.DLS(source,target,i)):
    #             return True
    #     return False




g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

source = 0
maxDepth = 2
target = 6

if g.DLS(source,target,maxDepth) == True:
    print("Target is reachable from the source within max depth")
else :
    print("Target is NOT reachable from the source within max depth")
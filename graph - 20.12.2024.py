class Graph:
    def __init__(self,n):
        self.n=n
        self.adj = [[]*n for i in range(n)]

    def createEdge(self,x,y): #x is start and y is end
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    
    def bfs(self,source):
        visited = [False] * self.n #none of the nodes are visited
        res = []
        queue = []

        queue.append(source)
        visited[source]=True #mark the source node as visited

        while len(queue)>0:
            s = queue.pop()
            res.append(s)

            for node in self.adj[s]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
        return res

graph = Graph(4)
graph.createEdge(1,2)
graph.createEdge(1,3)
graph.createEdge(2,4)
print(graph.bfs(0))


#DFS - Depth First Search

def dfs(graph, node, visit=None):
    if visit is None:
        visit = set()

    #Mark the current node as visited        
    visit.add(node)
    print(node, end=" ")

    #Recur down to the adjacent nodes that are not visited

    for neighbour in graph[node]:
        if neighbour not in visit:
            dfs(graph, neighbour, visit)

#test
graph={
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A","F"],
    "D":["B" , "E"],
    "E":["B"],
    "F":["C"]
}

dfs(graph,"A")
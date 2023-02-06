def DFS(start):
    cur = stck[len(stck)-1]
    for neighbor in edges[cur]:
        if (visited[neighbor] == False):
            stck.append(neighbor)
            visited[neighbor] = True
            print("stck:",stck)
            DFS(neighbor)
        else:
            path.append(stck.pop())
            print("stck:",stck)

start = 0
stck = [start]
path = []
edges = {
    0: [1,6],
    1: [2,0],
    2: [3,5,1],
    3: [4,2],
    4: [3],
    5: [2],
    6: [0]
}
visited = [True]+[False for i in range(len(edges)-1)]
DFS(0)
path.append(stck.pop())
print("stck:",stck)
print("path:",path)
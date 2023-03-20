def BFS(cur, done, end, reached):
    if (reached == False):
        if (done == True):
            return
        for neighbor in edges[cur]:
            if (visited[neighbor] == False):
                if (neighbor == end):
                    reached = True
                stck.append(neighbor)
                visited[neighbor] = True
                print("que:",stck, "\t reached = ", reached)
        path.append(stck.pop(0))
        print("que:",stck, "\t reached = ", reached)
        if (len(stck) == 0):
            return True
        done = BFS(stck[0], done, end, reached)
    elif (reached == True):
        if (len(stck)):
            path.append(stck.pop(0))
            print("que:",stck, "\t reached = ", reached)

reached = False
done = False
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
end = 5
visited = [True]+[False for i in range(len(edges)-1)]
BFS(stck[0], done, end, reached)
path.append(stck.pop(0))
print("que:", stck, "\t reached = ", reached)
print("path:",path)
def DFS(start, end):
    cur = stck[len(stck)-1]
    if (cur != end):
        for neighbor in edges[cur]:
            if (visited[neighbor] != True):
                stck.append(neighbor)
                visited[neighbor] = True
                print("stck:",stck)
                DFS(neighbor, end)
            else:
                path.append(stck.pop())
                print("stck:",stck)
    else:
        return

def last(ls):
    return ls[len(ls)-1]

def DF(end, reached):
    if reached == True:
        if (len(stck)):
            path.append(stck.pop())
        print("stck:", stck, "\t reached = ", reached)
    for neighbor in edges[last(stck)]:
        if (last(stck) != end and reached != True):
            if (visited[neighbor] != True):
                stck.append(neighbor)
                visited[neighbor] = True
                if (reached == True or last(stck) == end):
                    reached = True
                    print("stck:", stck, "\t reached = ", reached)
                    if (len(stck)):
                        path.append(stck.pop())
                    return reached
                print("stck:", stck, "\t reached = ", reached)
                reached = DF(end, reached)
            else:
                print("stck:", stck, "\t reached = ", reached)
                path.append(stck.pop())
        elif (reached == True):
            if (len(stck)):
                path.append(stck.pop())
            print("stck:", stck, "\t reached = ", reached)


start = 0
goal = 3
stck = [start]
path = []
edges = {
    0: [1,2,3],
    1: [3,4,0],
    2: [3,0],
    3: [0,1,2,5],
    4: [1,5],
    5: [3,5]
}
reached = False
visited = [True]+[False for i in range(len(edges)-1)]
DF(3, reached)
print("path:",path[::-1])
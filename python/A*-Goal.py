
if __name__=="__main__":
    h = {
        'A':9,
        'B':3,
        'C':2,
        'D':7,
        'E':4,
        'F':0
    }

    g = [
        ('A','B',3),('B','A',3),
        ('A','C',6),('C','A',6),
        ('A','D',2),('D','A',2),
        ('B','C',4),('C','B',4),
        ('C','E',1),('E','C',1),
        ('E','D',2),('D','E',2),
        ('D','F',9),('F','D',9)
    ]

    completed = False
    open = []
    close = []
    costs = []
    path = []
    start = 'A'
    end = 'F'
    open.append(start)
    cur = start
    steps = 10
    while not completed:
    # while steps:
        cur = open[0]
        possibleNodes = []
        possibleEdgesCosts = {}
        possiblePaths = []
        for edges in g:
            if (edges[0] == cur):
                possibleNodes.append(edges[1])
                possibleEdgesCosts[edges[1]] = edges[2]

        print(f"Cur : {cur}")
        print(f"possibleNodes : {possibleNodes}")
        print(f"possibleEdgesCosts : {possibleEdgesCosts}")
        
        for node in possibleNodes:
            hx = h[node]
            gx = possibleEdgesCosts[node]
            fx = gx + hx
            print(f"node:{node},fx:{fx},gx:{gx},hx:{hx}")
            possiblePaths.append((fx,cur,node))

        print(f"PossiblePaths: {possiblePaths}")
        print(f"PossiblePaths Size: {len(possiblePaths)}")
        
        sameCombinations = []
        for combination in possiblePaths:
            if (combination[2] in close):
                sameCombinations.append(combination)
        
        possiblePaths = list(set(possiblePaths) - set(sameCombinations))


        print(f"PossiblePaths After Removing Visited: {possiblePaths}")
        minPossiblePath = min(possiblePaths)


        print(f"Min Path : {minPossiblePath}")
        open.append(minPossiblePath[2])
        close.append(minPossiblePath[1])
        costs.append(minPossiblePath[0])

        open.pop(0)
        if (open[0] == end):
            completed = True
        steps -= 1
        print("\n\n")
        print(f"Open : f{open}")
        print(f"Close : f{close}")
        print(f"Costs : f{costs}")
        print("\n\n")
    print("Completed!!!")
    close.append(end)
    print(f"PATHS : {close}")
def ham(ls1,ls2):
    dis = 0
    for i in range(len(ls1)):
        if (ls1[i]!=ls2[i]):
            dis+=1
    return dis

def getInvCount(ls):
    blank = 0
    inv = 0
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if (ls[j] != blank and ls[i] != blank and ls[i] > ls[j]):
                inv += 1
    return inv%2==0

def swap(move,curVal,ind):
    if (move == "up"):
        nextInd = ind-3
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal
    if (move == "down"):
        nextInd = ind+3
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal
    if (move == "left"):
        nextInd = ind-1
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal
    if (move == "right"):
        nextInd = ind+1
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal


def best(cur,LastMove):
    moves = {
        "up" : [3,4,5,6,7,8],
        "down" : [0,1,2,3,4,5],
        "left" : [1,2,4,5,7,8],
        "right" : [0,1,3,4,6,7]
    }

    ind0 = cur.index(0)
    

    possibleMoves = []
    possibleMoves.append("a_up" if ind0 in moves["up"] else "-")
    possibleMoves.append("b_down" if ind0 in moves["down"] else "-")
    possibleMoves.append("c_left" if ind0 in moves["left"] else "-")
    possibleMoves.append("d_right" if ind0 in moves["right"] else "-")

    print(f"possibleMoves: {possibleMoves}")

    possiblePaths = []

    print("Position of '0' : ", ind0)
    print("CUR in best : ", cur)
    if "a_up" in possibleMoves:
        copyCurUp = cur.copy()
        copyCurUp = swap("up",copyCurUp,ind0)
        print("Possible Move Up: ")
        printLs(copyCurUp)
        h = ham(initial,copyCurUp)
        g = ham(copyCurUp,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"a_up"))

    if "b_down" in possibleMoves:
        copyCurDown = cur.copy()
        copyCurDown = swap("down",copyCurDown,ind0)
        print("Possible Move Down: ")
        printLs(copyCurDown)
        h = ham(initial, copyCurDown)
        g = ham(copyCurDown,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"b_down"))
    
    if "c_left" in possibleMoves:
        copyCurLeft = cur.copy()
        copyCurLeft = swap("left",copyCurLeft,ind0)
        print("Possible Move Left: ")
        printLs(copyCurLeft)
        h = ham(initial, copyCurLeft)
        g = ham(copyCurLeft,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"c_left"))

    if "d_right" in possibleMoves:
        copyCurRight = cur.copy()
        copyCurRight = swap("right",copyCurRight,ind0)
        print("Possible Move Right: ")
        printLs(copyCurRight)
        h = ham(initial, copyCurRight)
        g = ham(copyCurRight,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"d_right"))
    
    print(f"possiblePaths and their values : {possiblePaths}")
    if (lastMove != ""):
        if (lastMove in ["a_up","b_down"]):
            notMove = "a_up" if lastMove == "b_down" else "b_down"
        elif (lastMove in ["c_left","d_right"]):
            notMove = "left" if lastMove == "d_right" else "d_right"
        print("Last Move : ", lastMove)
        print("Not Move : ", notMove)
        print("Thus removing compliment of LastMove from possiblePaths...")
        for i in possiblePaths:
            if i[1] == notMove:
                possiblePaths.remove(i)
        print(f"possiblePaths and their values after removing lastmove: {possiblePaths}")
    
    # removing paths which are visited
    for i in possiblePaths:
        if (i in visited):
            possiblePaths.remove(i)
    print(f"possiblePaths and their values after Visited : {possiblePaths}")

    
    minPath = min(possiblePaths)
    print(f"Min : {minPath}")
    if (minPath[1] == "a_up"):
        visited.append(copyCurUp)
        return copyCurUp,"a_up"
    if (minPath[1] == "b_down"):
        visited.append(copyCurDown)
        return copyCurDown,"b_down"
    if (minPath[1] == "c_left"):
        visited.append(copyCurLeft)
        return copyCurLeft,"c_left"
    if (minPath[1] == "d_right"):
        visited.append(copyCurRight)
        return copyCurRight,"d_right"


def printLs(ls):
    for i in range(len(ls)):
        print("{:<5}".format(ls[i]), end=" ")
        if (i == 2 or i == 5 or i == 8): print('\n')


if __name__ == "__main__":
    goal = [
        1,2,3,
        4,5,6,
        7,8,0
    ]
    initial = [
        1,8,2,
        0,4,3,
        7,6,5
    ]

    cur = initial
    lastMove = ""
    steps = 10
    visited = [initial]
    # while (True):
    while (steps):
        isSolvable = getInvCount(cur)
        print(f"Is is solvable : {getInvCount(cur)}")
        if (not isSolvable):
            print(f"Is is solvable : {getInvCount(cur)}")
            break
        
        print("\n\n")
        print("CUR : ")
        printLs(cur)
        # print(cur)
        # print(goal)
        print("Is cur == goal ? :", cur == goal)
        print("Hamming Distance : ",ham(cur,goal))
        cur,lastMove = best(cur,lastMove)
        if (cur == goal):
            break
        steps -= 1

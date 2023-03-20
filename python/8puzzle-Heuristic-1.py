def ham(ls1,ls2):
    dis = 0
    for i in range(len(ls1)):
        if (ls1[i]!=ls2[i]):
            dis+=1
    return dis

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


def best(cur,LastMove,step):
    moves = {
        "up" : [3,4,5,6,7,8],
        "down" : [0,1,2,3,4,5],
        "left" : [1,2,4,5,7,8],
        "right" : [0,1,3,4,6,7]
    }

    ind0 = cur.index(0)

    possibleMoves = []
    possibleMoves.append("up" if ind0 in moves["up"] else "-")
    possibleMoves.append("down" if ind0 in moves["down"] else "-")
    possibleMoves.append("left" if ind0 in moves["left"] else "-")
    possibleMoves.append("right" if ind0 in moves["right"] else "-")

    print(f"possibleMoves: {possibleMoves}")

    possiblePaths = []

    print("Position of '0' : ", ind0)
    print("CUR in best : ", cur)
    if "up" in possibleMoves:
        copyCurUp = cur.copy()
        copyCurUp = swap("up",copyCurUp,ind0)
        print("Possible Move Up: ")
        printLs(copyCurUp)
        g = step
        h = ham(goal, copyCurUp)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"up"))

    if "down" in possibleMoves:
        copyCurDown = cur.copy()
        copyCurDown = swap("down",copyCurDown,ind0)
        print("Possible Move Down: ")
        printLs(copyCurDown)
        g = step
        h = ham(goal, copyCurDown)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"down"))
    
    if "left" in possibleMoves:
        copyCurLeft = cur.copy()
        copyCurLeft = swap("left",copyCurLeft,ind0)
        print("Possible Move Left: ")
        printLs(copyCurLeft)
        g = step
        h = ham(goal, copyCurLeft)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"left"))

    if "right" in possibleMoves:
        copyCurRight = cur.copy()
        copyCurRight = swap("right",copyCurRight,ind0)
        print("Possible Move Right: ")
        printLs(copyCurRight)
        g = step
        h = ham(goal, copyCurRight)
        f = h+g
        print("F,G,H :", f,g,h)
        possiblePaths.append((f,"right"))
    
    print(f"possiblePaths and their values : {possiblePaths}")
    if (lastMove != ""):
        if (lastMove in ["up","down"]):
            notMove = "up" if lastMove == "down" else "down"
        elif (lastMove in ["left","right"]):
            notMove = "left" if lastMove == "right" else "right"
        print("Last Move : ", lastMove)
        print("Not Move : ", notMove)
        print("Thus removing compliment of LastMove from possiblePaths...")
        for i in possiblePaths:
            if i[1] == notMove:
                possiblePaths.remove(i)
        print(f"possiblePaths and their values : {possiblePaths}")

    
    minPath = min(possiblePaths)
    print(f"Min : {minPath}")
    if (minPath[1] == "up"):
        return copyCurUp,"up"
    if (minPath[1] == "down"):
        return copyCurDown,"down"
    if (minPath[1] == "left"):
        return copyCurLeft,"left"
    if (minPath[1] == "right"):
        return copyCurRight,"right"


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
        1,2,3,
        4,0,6,
        5,7,8
    ]

    cur = initial
    lastMove = ""
    step = 1
    while (True):
        print("\n\n")
        print("CUR : ")
        printLs(cur)
        # print(cur)
        # print(goal)
        print("Is cur == goal ? :", cur == goal)
        print("Hamming Distance : ",ham(cur,goal))
        cur,lastMove = best(cur,lastMove,step)
        if (cur == goal):
            break
        step += 1

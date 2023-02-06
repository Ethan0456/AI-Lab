def winningCaseOrRandomLoc():
    remLoc = fetchRemLoc()
    print(remLoc)
    for tup in remLoc:
        i,j = tup[0],tup[1]
        print(i,j)
        try:
            # for dis in range(1,3):
                # if (mat[i-dis][j-dis] == mat[i+dis][j+dis] == 1) or (mat[i-dis][j] == mat[i+dis][j] == 1) or (mat[i][j-dis] == mat[i][j+dis] == 1):
                #     return i,j
                
            if (mat[i-1][j-1] == mat[i+1][j+1] == 1):
                print("in center backward slash")
                return i,j
            if (mat[i-1][j+1] == mat[i+1][j-1] == 1):
                print("in center forward slash")
                return i,j
            if (mat[i-1][j] == mat[i+1][j] == 1):
                print("in center vertical")
                return i,j
            if (mat[i][j-1] == mat[i][j+1] == 1):
                print("in center horizontal")
                return i,j
            if (mat[i][j+1] == mat[i][j+2] == 1):
                print("in left corner horizontal")
                return i,j
            if (mat[i][j-1] == mat[i][j-2] == 1):
                print("in right corner horizontal")
                return i,j
            if (mat[i+1][j] == mat[i+2][j] == 1):
                print("in up corner vertical")
                return i,j
            if (mat[i-1][j] == mat[i-2][j] == 1):
                print("in down corner vertical")
                return i,j
        except IndexError:
            pass

def fetchRemLoc():
    remLoc = []
    for row in range(len(mat)):
        for ele in range(len(mat)):
            if mat[row][ele] == -1:
                remLoc.append((row, ele))
    return remLoc

mat = [
    [-1,-1,1],
    [-1,-1,1],
    [1,-1,-1]
]

print("win : ",winningCaseOrRandomLoc())

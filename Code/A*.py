import numpy as np

def heuristic(x,y):
    try:
        right = np.array(x,y+1) # 3
        down = np.array(x+1,y)  # 1
        up = np.array(x-1,y)    # 0
        left = np.array(x,y-1)  # 2

        nextCell = [
            abs(up.subract(start))+abs(up-stop),
            abs(down-start)+abs(down-stop),
            abs(left-start)+abs(left-stop),
            abs(right-start)+abs(right-stop)
        ]
        return nextCell.index(min(nextCell))
    except IndexError:
        pass


if __name__ == "__main__":
    start = (0,0)
    stop = (3,3)

    ls = [
        {'S':-1,0:-1,0:-1,0:-1},
        {0:-1,0:-1,0:-1,0:-1},
        {0:-1,0:-1,0:-1,0:-1},
        {0:-1,0:-1,0:-1,0:'G'},
    ]
    # current = 0
    # visited = 1
    # visited and used = 2
    # visited and not used = 3
    completed = False

    cur = start
    while(not completed):
        next = heuristic(cur[0], cur[1])
        if (next == 0):
            cur = (cur[0], cur[1]+1)
        elif (next == 1):
            cur = (cur[0]+1, cur[1])
        elif (next == 2):
            cur = (cur[0]-1, cur[1])
        else: 
            cur = (cur[0], cur[1]-1)
        
        if (cur == stop): completed = True
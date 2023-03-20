import math
import time

states = [(0,0)]
possibleStates = []

def rules():
    if (a<capA):
        possibleStates.append((capA,b))
    if (b<capB):
        possibleStates.append((a,capB))
    if (a>0):
        possibleStates.append((0,b))
    if (b>0):
        possibleStates.append((a,0))
    if (a+b)>=capA and (b>0):
        possibleStates.append((capA,b-(capA-a)))
    if (a+b)>=capB and (a>0):
        possibleStates.append((a-(capB-b),b))
    if (a+b)<=capB and (b>0):
        possibleStates.append((a+b,0))
    if (a+b)<=capB and (a>0):
        possibleStates.append((0,a+b))

if __name__=="__main__":
    capA = int(input("Enter Capacity of Jug A : "))
    capB = int(input("Enter Capacity of Jug B : "))
    tar = int(input("Enter Target Value : "))
    a = 0
    b = 0

    if (tar > max(capA, capB)):
        print("Invalid Target Value")
        exit

    if (math.gcd(capA,capB)%tar == 0):
        print("Not Possible With this numbers!")
        exit

    start = time.time()
    while (max(a,b) != tar):
        a,b = states[0][0],states[0][1]

        rules()

        complete=0
        for i in possibleStates:
            if (i[0]==tar or i[1]==tar):
                print("GOT TARGET")
                complete=1
            if (i not in states):
                states.append(i)
                print(i)
        if complete==1:
            break

        states.pop(0)
        possibleStates.clear()
    stop = time.time() - start
    print(f"Time : {stop}")
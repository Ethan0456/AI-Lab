from random import *

def runner():
    print(ls)
    for i in range(3):
        try:
            if ((ls[i]+ls[i+1]+ls[i+2]) in [1,3]):
                return (i,i+1,i+2)
            if ((ls[i]+ls[i+2]+ls[i+4]) in [1,3]) and i>1:
                return (i,i+2,i+4)
            if ((ls[i]+ls[i+3]+ls[i+6]) in [1,3]):
                return (i,i+3,i+6)
            if ((ls[i]+ls[i+4]+ls[i+8]) in [1,3]):
                return (i,i+4,i+8)
        except IndexError:
            pass

def randomValue():
    print("Choosing random--->")
    tmp = randint(0,8)
    while (ls[tmp] != -1): tmp = randint(0,8)
    ls[tmp] = comp

def smartRandom():
    for i in range(len(ls)):
        if (ls[i] == 1):
            if (ls[i-1]==-1):
                print("Smart Random----->")
                ls[i-1] = 1
                return
            if (ls[i+1]==-1):
                print("Smart Random----->")
                ls[i+1] = 1
                return
    randomValue()


def main():
    tup = runner()
    if (tup == None):
        print()
        smartRandom()
    else:
        for i in tup:
            if (ls[i] == -1):
                ls[i] = comp

def checkIfCompleted():
    for i in range(3):
        try:
            if (i==0) and (ls[i]==ls[i+1]==ls[i+2]==1) or (ls[i]==ls[i+1]==ls[i+2]==2):
                return "Consecutive(Row)"
            if (ls[i]==ls[i+2]==ls[i+4]==1) or (ls[i]==ls[i+2]==ls[i+4]==2):
                return "Forward Slash"
            if (ls[i]==ls[i+3]==ls[i+6]==1) or (ls[i]==ls[i+3]==ls[i+6]==2):
                return "Vertical(Column)"
            if (ls[i]==ls[i+4]==ls[i+8]==1) or (ls[i]==ls[i+4]==ls[i+8]==2):
                return "Backward Slash"
        except IndexError:
            pass


def printLs():
    for i in range(len(ls)):
        print("{:<5}".format(ls[i]), end=" ")
        if (i == 2 or i == 5 or i == 8): print('\n')

ls = [
    -1, -1, -1,
    -1, -1, -1,
    -1, -1, -1
    ]

if __name__=="__main__":
    comp = 1
    human = 2
    completed = False

    while not completed:
        printLs()
        loc = int(input("Enter Location as 1D array: "))
        if (ls[loc] == -1):
            ls[loc] = human
            main()
        else:
            print()
            print("Invalid Location!")

        strf = checkIfCompleted()
        if (strf != None):
            print()
            print("Complete!")
            print(strf)
            printLs()
            print()
            break
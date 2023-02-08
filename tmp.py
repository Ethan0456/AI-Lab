# def winningCaseOrRandomLoc():
#     remLoc = fetchRemLoc()
#     print(remLoc)
#     for tup in remLoc:
#         i,j = tup[0],tup[1]
#         print(i,j)
#         try:
#             # for dis in range(1,3):
#                 # if (mat[i-dis][j-dis] == mat[i+dis][j+dis] == 1) or (mat[i-dis][j] == mat[i+dis][j] == 1) or (mat[i][j-dis] == mat[i][j+dis] == 1):
#                 #     return i,j
                
#             if (mat[i-1][j-1] == mat[i+1][j+1] == 1):
#                 print("in center backward slash")
#                 return i,j
#             if (mat[i-1][j+1] == mat[i+1][j-1] == 1):
#                 print("in center forward slash")
#                 return i,j
#             if (mat[i-1][j] == mat[i+1][j] == 1):
#                 print("in center vertical")
#                 return i,j
#             if (mat[i][j-1] == mat[i][j+1] == 1):
#                 print("in center horizontal")
#                 return i,j
#             if (mat[i][j+1] == mat[i][j+2] == 1):
#                 print("in left corner horizontal")
#                 return i,j
#             if (mat[i][j-1] == mat[i][j-2] == 1):
#                 print("in right corner horizontal")
#                 return i,j
#             if (mat[i+1][j] == mat[i+2][j] == 1):
#                 print("in up corner vertical")
#                 return i,j
#             if (mat[i-1][j] == mat[i-2][j] == 1):
#                 print("in down corner vertical")
#                 return i,j
#         except IndexError:
#             pass

# def fetchRemLoc():
#     remLoc = []
#     for row in range(len(mat)):
#         for ele in range(len(mat)):
#             if mat[row][ele] == -1:
#                 remLoc.append((row, ele))
#     return remLoc

# mat = [
#     [-1,-1,1],
#     [-1,-1,1],
#     [1,-1,-1]
# ]

# print("win : ",winningCaseOrRandomLoc())

import pandas as pd

df = pd.DataFrame([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20],
    [21,22,23,24],
    [25,26,27,28],
    [29,30,31,32]
]
)

print(df)
print(df.iloc[[1,3,6]])
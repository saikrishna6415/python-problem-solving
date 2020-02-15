mat = []
def creatematrix(m,x,y):
    for i in range(m):
        temp = [ ]
        for j in range(m):
            if i == x and j == y:
                temp.append("R")
            else:
                temp.append("*")
        mat.append(temp)
    return mat

def upper(m,x,y):
    temp = [ ]
    i = x-1
    while i >= 0:
        mat[i][y]="."
        temp.append([i,y])
        i-=1
    return temp

def lower(m,x,y):
    temp =[ ]
    i = x+1
    while i < m:
        mat[i][y]="."
        temp.append([i,y])
        i+=1
    return temp

def left(m,x,y):
    temp = [ ]
    i = y-1
    while i >=0:
        mat[x][i] = "."
        temp.append([x,i])
        i-=1
    return temp

def right(m,x,y):
    temp =[ ]
    i = y+1
    while i < m:
        mat[x][i]="."
        temp.append([x,i])
        i+=1
    return temp



def rookmoves(m,x,y):
    creatematrix(m,x,y)
    print("the possible moves by rook are : ")
    print(upper(m,x,y))
    print(lower(m,x,y))
    print(left(m,x,y))
    print(right(m,x,y))
    print()
    for i in mat:
         print(i)


rookmoves(8,2,6)

# the possible moves by rook are :
# [[3, 4], [2, 4], [1, 4], [0, 4]]
# [[5, 4], [6, 4], [7, 4]]
# [[4, 3], [4, 2], [4, 1], [4, 0]]
# [[4, 5], [4, 6], [4, 7]]

# ['*', '*', '*', '*', '.', '*', '*', '*']
# ['*', '*', '*', '*', '.', '*', '*', '*']
# ['*', '*', '*', '*', '.', '*', '*', '*']
# ['*', '*', '*', '*', '.', '*', '*', '*']
# ['.', '.', '.', '.', 'R', '.', '.', '.']
# ['*', '*', '*', '*', '.', '*', '*', '*']
# ['*', '*', '*', '*', '.', '*', '*', '*']
# ['*', '*', '*', '*', '.', '*', '*', '*']
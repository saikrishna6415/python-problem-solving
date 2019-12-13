mat = [ ]
def creatematrix(m,x,y):
    for i in range(m):
        temp = [ ]
        for j in range(m):
            if i == x and j == y:
                temp.append("K")
            else:
                temp.append("0")
        mat.append(temp)
    return mat

def upper(m,x,y):
    temp = [ ]
    i = x-1
    if i >= 0:
        mat[i][y]="."
        temp.append([i,y])
    return temp

def lower(m,x,y):
    temp =[ ]
    i = x+1
    if i < m:
        mat[i][y]="."
        temp.append([i,y])
    return temp

def left(m,x,y):
    temp = [ ]
    i = y-1
    if i >=0:
        mat[x][i] = "."
        temp.append([x,i])
    return temp

def right(m,x,y):
    temp =[ ]
    i = y+1
    if i < m:
        mat[x][i]="."
        temp.append([x,i])
    return temp

def leftupperdiagonal(m,x,y):
    temp =[ ]
    i = x-1
    j = y-1
    if i >= 0 and j >= 0:
        mat[i][j]="."
        temp.append([i,j])
    return temp

def rightupperdiagonal(m,x,y):
    temp = [ ]
    i = x-1
    j = y+1
    if i >=0 and j < m:
        mat[i][j]='.'
        temp.append([i,j])
    return temp

def leftlowerdiagonal(m,x,y):
    temp = [ ]
    i = x+1
    j= y-1
    if i < m  and j >= 0:
        mat[i][j] = "."
        temp.append([i,j])
    return temp


def rightlowerdiagonal(m,x,y):
    temp=[]
    i = x+1
    j = y+1
    if i < m and j < m:
        mat[i][j] = '.'
        temp.append([i,j])
    return temp

def kingmoves(m,x,y):
    creatematrix(m,x,y)
    print("the possible moves by king are : ")
    print(upper(m,x,y))
    print(lower(m,x,y))
    print(left(m,x,y))
    print(right(m,x,y))
    print(leftupperdiagonal(m,x,y))
    print(rightupperdiagonal(m,x,y))
    print(leftlowerdiagonal(m,x,y))
    print(rightlowerdiagonal(m,x,y))
    print()
    for i in mat:
         print(i)


kingmoves(8,7,7)



# output
# [4, 1]]
# []
# []
# []
# []
# []
# [[5, 2]]
# [[7, 2]]

# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ']
# ['K', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ']
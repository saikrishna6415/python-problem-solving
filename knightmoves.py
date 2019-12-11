mat = []
def creatematrix(m,x,y):
    for i in range(m):
        temp = [ ]
        for j in range(m):
            if i == x and j == y:
                temp.append("K")
            else:
                temp.append(" ")
        mat.append(temp)
    return mat

def upleft(m,x,y):
    temp = [ ]
    i = x-2
    j = y-1
    if i >= 0 and j >=0:
        mat[i][j]="#"
        temp.append([i,y])
    return temp

def upright(m,x,y):
    temp =[ ]
    i = x-2
    j = y+1
    if  i >= 0 and j < m:
        mat[i][j]="#"
        temp.append([i,j])
    return temp

def leftup(m,x,y):
    temp = [ ]
    i = x-1
    j = y-2
    if i >=0  and j >= 0:
        mat[i][j] = "#"
        temp.append([i,j])
    return temp

def leftdown(m,x,y):
    temp =[ ]
    i = x+1
    j = y-2
    if i < m and j >= 0:
        mat[i][j]="#"
        temp.append([i,j])
    return temp

def downleft(m,x,y):
    temp =[ ]
    i = x+2
    j = y-1
    if (i < m  and j >= 0):
        mat[i][j]="#"
        temp.append([i,j])
    return temp

def downright(m,x,y):
    temp = [ ]
    i = x+2
    j = y+1
    if(i < m and j < m):
        mat[i][j]='#'
        temp.append([i,j])

    return temp

def rightdown(m,x,y):
    temp = [ ]
    i = x+1
    j= y+2
    if( i >= 0 and i < m and j < m ):
        mat[i][j] = "#"
        temp.append([i,j])
    return temp


def rightup(m,x,y):
    temp=[]
    i = x-1
    j = y+2
    if (i < m  and i >=0 and j >= 0 and j< m):
        mat[i][j] = '#'
        temp.append([i,j])
    
    return temp

def knightmoves(m,x,y):
    creatematrix(m,x,y)
    print("the possible moves by Knight are : ")
    print(upright(m,x,y))
    print(upleft(m,x,y))
    print(leftup(m,x,y))
    print(leftdown(m,x,y))
    print(downleft(m,x,y))
    print(downright(m,x,y))
    print(rightup(m,x,y))
    print(rightdown(m,x,y))
    print()
    for i in mat:
         print(i)


knightmoves(8,6,0)
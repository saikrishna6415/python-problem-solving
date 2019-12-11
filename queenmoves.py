mat = []
def creatematrix(m,x,y):
    for i in range(m):
        temp = [ ]
        for j in range(m):
            if i == x and j == y:
                temp.append("Q")
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

def leftupperdiagonal(m,x,y):
    temp =[ ]
    i = x-1
    j = y-1
    while(i >= 0 and j >= 0):
        mat[i][j]="."
        temp.append([i,j])
        i-=1
        j-=1
    return temp

def rightupperdiagonal(m,x,y):
    temp = [ ]
    i = x-1
    j = y+1
    while (i >=0 and j < m):
        mat[i][j]='.'
        temp.append([i,j])
        i-=1
        j+=1
    return temp

def leftlowerdiagonal(m,x,y):
    temp = [ ]
    i = x+1
    j= y-1
    while( i < m  and j >= 0):
        mat[i][j] = "."
        temp.append([i,j])
        i+=1
        j-=1
    return temp


def rightlowerdiagonal(m,x,y):
    temp=[]
    i = x+1
    j = y+1
    while (i < m and j < m):
        mat[i][j] = '.'
        temp.append([i,j])
        i+=1
        j+=1
    return temp

def queen(m,x,y):
    creatematrix(m,x,y)
    print("the possible moves by Queen are : ")
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


queen(8,4,4)
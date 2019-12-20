mat = []
possibleways = [ ]

def creatematrix(m,x,y,r,c):
    for i in range(m):
        temp = [ ]
        for j in range(m):
            if i == x and j == y:
                temp.append("Q")
            else:
                temp.append("*")
        mat.append(temp)
    return mat

def upper(m,x,y,r,c):
    temp = [ ]
    i = x-1
    while i >= 0 :
        mat[i][y]="."
        temp.append([i,y])
        i-=1
    return temp

def lower(m,x,y,r,c):
    temp =[ ]
    i = x+1
    while i < m :
        mat[i][y]="."
        temp.append([i,y])
        i+=1
    return temp

def left(m,x,y,r,c):
    temp = [ ]
    i = y-1
    while i >=0:
        mat[x][i] = "."
        temp.append([x,i])
        i-=1
    return temp

def right(m,x,y,r,c):
    temp =[ ]
    i = y+1
    while i < m and  i <= c :
        mat[x][i]="."
        temp.append([x,i])
        i+=1
    return temp

def leftupperdiagonal(m,x,y,r,c):
    temp =[ ]
    i = x-1
    j = y-1
    while(i >= 0 and j >= 0):
        mat[i][j]="."
        temp.append([i,j])
        i-=1
        j-=1
    return temp

def rightupperdiagonal(m,x,y,r,c):
    temp = [ ]
    i = x-1
    j = y+1
    
    while (i >=0 and j < m and i<=c) :
        mat[i][j]='.'
        temp.append([i,j])
        i-=1
        j+=1
    return temp

def leftlowerdiagonal(m,x,y,r,c):
    temp = [ ]
    i = x+1
    j= y-1
    while( i < m  and j >= 0) :
        mat[i][j] = "."
        temp.append([i,j])
        i+=1
        j-=1
    return temp


def rightlowerdiagonal(m,x,y,r,c):
    temp=[]
    i = x+1
    j = y+1
    while (i < m and j < m ):
        mat[i][j] = '.'
        temp.append([i,j])
        i+=1
        j+=1
    return temp

def queen(m,x,y,r,c):
    creatematrix(m,x,y,r,c)
    print("the possible moves by Queen are : ")
    print(upper(m,x,y,r,c))
    print(lower(m,x,y,r,c))
    print(left(m,x,y,r,c))
    print(right(m,x,y,r,c))
    print(leftupperdiagonal(m,x,y,r,c))
    print(rightupperdiagonal(m,x,y,r,c))
    print(leftlowerdiagonal(m,x,y,r,c))
    print(rightlowerdiagonal(m,x,y,r,c))
    print()
    mat[r][c]="A"
    for i in range(len(mat)):
        print(mat[i])
        possibleways.append(mat[i].count('.'))

    print(sum(possibleways))

queen(8,3,3,3,6)

mat = [ ]
def creatematrix(m,x,y):
    for i in range(m):
        temp = [ ]
        for j in range(m):
            if i == x and j == y:
                temp.append("B")
            else:
                temp.append("0")
        mat.append(temp)
    return mat


def leftupperdiagonal(m,x,y):
    temp =[ ]
    i = x-1
    j = y-1
    while i >= 0 and j >= 0:
        mat[i][j]="."
        temp.append([i,j])
        i-=1
        j-=1
    return temp

def rightupperdiagonal(m,x,y):
    temp = [ ]
    i = x-1
    j = y+1
    while i >=0 and j < m:
        mat[i][j]='.'
        temp.append([i,j])
        i-=1
        j+=1
    return temp

def leftlowerdiagonal(m,x,y):
    temp = [ ]
    i = x+1
    j= y-1
    while i < m  and j >= 0:
        mat[i][j] = "."
        temp.append([i,j])
        i+=1
        j-=1
    return temp


def rightlowerdiagonal(m,x,y):
    temp=[]
    i = x+1
    j = y+1
    while i < m and j < m:
        mat[i][j] = '.'
        temp.append([i,j])
        i+=1
        j+=1
    return temp

def bishopmoves(m,x,y):
    creatematrix(m,x,y)
    print("the possible moves by bishop are : ")
    print(leftupperdiagonal(m,x,y))
    print(rightupperdiagonal(m,x,y))
    print(leftlowerdiagonal(m,x,y))
    print(rightlowerdiagonal(m,x,y))
    print()
    for i in mat:
         print(i)


bishopmoves(8,4,4)
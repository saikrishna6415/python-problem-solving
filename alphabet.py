n=int(input())
for i in range(n):
    for row in range(7):
        for col in range(6):
            if( row in {0,1,2,4,5,6}) and (col in {0,5}):
                print('*',end=" ")
            elif( row==3):
                print("*",end= " ")
            else:
                 print(" ",end=" ")
        print()


# OUTPUT
# 2
# *         *
# *         *
# *         *
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# *         *
# *         *
# * * * * * *
# *         *
# *         *
# *         *
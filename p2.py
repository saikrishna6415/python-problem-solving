# n=int(input())
# for i in range(n):
#     print((str(n)+ "" ) *n)

# for i in range(n):
#     print((str(n)+ "" ) *(i+1))

# for i in range(n):
#     print((str(i+1)+ "" ) *n)

# for i in range(n):
#     print((chr(65+i)+ " " ) *n)

# for i in range(n):
#     print((chr(65+i)+ " " ) *(i+1))

# for i in range(n):
#     print((str(n)+ "" ) *(n-i))

# for i in range(n):
#     for j in range(i):
#         print(j+1,end=" ")
#     print( )

# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end=" ")
#     print( )

# for i in range(n):
#     print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))


# for i in range(n):
#     print(' '*(n-i-1)+ (i+1)*"* ")
# for i in range(n-1):
#     print((i)*" "+" *"*(n-i-1))

for row in range(7):
    for col in range(5):
        if (row==0 )and (col in {1,2,3}):
            print("*",end=" ")
        elif( row in {1,2,4,5,6}) and (col in {0,4}):
            print('*',end=" ")
        elif( row==3):
            print("*",end= " ")
        else:
            print(" ",end=" ")
    print()


#   * * *
# *       *
# *       *
# * * * * *
# *       *
# *       *
# *       *
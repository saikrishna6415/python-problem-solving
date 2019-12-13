n = int(input("enter number : "))


for i in range(1,n+1):
    print((n-i)*" ",end=" ")
    for j in range(1,i+1):
        if i %2==0:
            print(str(j)+" ",end="")
        else:
            print("* ",end="")
    print()

# enter number : 5
#      *
#     1 2
#    * * *
#   1 2 3 4
#  * * * * *
n = int(input("enter a number : "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i ==n//2 or (j==0 and i < n//2) or ( j ==n-1 and i >=n//2 ):
            print("*",end=" ")
        else:
            print("  ",end="")
    print()

# enter a number : 5
# * * * * *
# *
# * * * * *
#         *
# * * * * *
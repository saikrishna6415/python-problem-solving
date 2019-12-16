n =int(input("enter a number : "))
for i in range(1,n+1):
    print((n-i)*" ",end="")
    for j in range(1,i+1):
        if i == 1 or i ==n or j ==1 or i ==j:
            print(str(j)+" ",end="")
        else:
            print("  ",end="")
    print()

# enter a number : 4
#    1
#   1 2
#  1   3
# 1 2 3 4
n = int(input("enter number : "))

for i in range(1,n+1):
    if i % 3==1:
        print("* ",end="")
    elif i % 3 ==2:
        print("# ",end="")
    else:
        print("@ ",end="")
    

# enter number : 6
# * # @ * # @
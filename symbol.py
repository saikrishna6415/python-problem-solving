n = int(input("enter number : "))

for i in range(n):
    if i % 2==0:
        print("* ",end="")
    else:
        print("# ",end="")
    

# enter number : 4
# * # * #
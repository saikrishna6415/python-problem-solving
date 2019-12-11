n = int(input("enter number : "))

for i in range(1,n+1):
    for j in range(i):
        if j % 3 == 0:
            print("* ",end="")
        elif j % 3 == 1:
            print("# ",end="")
        else:
            print("@ ",end="")
    print()

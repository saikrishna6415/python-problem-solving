n = int(input("enter number : "))

for i in range(1,n+1):
    for j in range(n,1,-1):
        if j <= i:
            print(str(i)+" ",end="")
        else:
            print(str(1)+" ",end="")
    print()

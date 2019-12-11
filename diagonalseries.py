n = int(input("enter number : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j :
            print(j,end="")
        else:
            print(0,end="")
    print()

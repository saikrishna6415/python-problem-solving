n = int(input("enter number : "))

for i in range(1,n+2):
    if i % 2 == 0:
        for j in range(i,0,-1):
            print(j,end="")
        print("*",end="")
    else:
        print("*",end="")
        for j in range(1,i+1):
            print(j,end="")
    print()


 
n = int(input("enter number : "))

for  i in range(n,0,-1):
    for j in range(i,0,-1):
        print(str(j)+" ",end="")
    print()
for  i in range(n,0,-1)[::-1]:
    for j in range(i,0,-1):
        print(str(j)+" ",end="")
    print()
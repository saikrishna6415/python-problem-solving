n = int(input("enter number : "))

for  i in range(n,0,-1):
    print((n-i)*" ",end="")
    for j in range(i,0,-1):
        print(str(n-j+1)+" ",end="")
    print()
for  i in range(n,0,-1)[::-1]:
    print((n-i)*" ",end="")
    for j in range(i,0,-1):
        print(str(n-j+1)+" ",end="")
    print()

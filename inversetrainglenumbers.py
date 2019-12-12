n = int(input("enter a number: "))
a=1
for i in range(1,n+1):
    print(i*" ",end=" ")
    for j in range(n-i+1):
        print((str(a)+" "),end="")
        a+=(n-j)
    print()
    a=i+1
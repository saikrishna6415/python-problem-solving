n = int(input("enter number : "))

for i in range(n):
    for j in range(i):
        if j % 2 ==0:
            print(1,end="")
        else:
            print(0,end="")
    print()

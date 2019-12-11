n = int(input("enter number : "))

for i in range(1,n+1):
    if i % 2 == 0:
        print(str(2**i) + " ",end="")
    else:
        print("* ",end="")

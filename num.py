n = int(input("enter a number : "))

for i in range(1,n+1):
    if i % 2 ==1:
        print("*",end="")
        for j in range(1,i+1):
            print(j ,end="")
    else:
        for j in range(1,i+1):
            print(j,end="")
            print("*")

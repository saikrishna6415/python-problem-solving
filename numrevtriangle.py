n = int(input("enter a number :"))

for i in range(1,n+1):
    print((n-i)*" ",end="")
    k=i
    for j in range(1,i+1):
        print(k,end="")
        k+=1
    k=i
    for  j in range(1,i):
        print(k,end="")
        k+=1
    print()

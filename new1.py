n = int(input("enter number : "))

for i in range(1,n+1):
    for j in range(2*i-1):
        print(i+j*4,end=" ")
    print()
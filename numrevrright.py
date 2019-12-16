n = int(input("enter a number : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()

    

# enter a number : 4
# 1
# 121
# 12321
# 1234321
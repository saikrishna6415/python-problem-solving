n = int(input("enter a number : "))

for i in range(n):
    for j in range(i,n):
        if j == i or i ==0 or j==n-1:
            print(str(j+1)+" ",end="")
        else:
            print("  ",end="")
    print()
# enter a number : 10
# 1 2 3 4 5 6 7 8 9 10
# 2               10
# 3             10
# 4           10
# 5         10
# 6       10
# 7     10
# 8   10
# 9 10
# 10

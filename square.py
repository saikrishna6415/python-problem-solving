n = int(input(" enter a  number : "))

for i in range(n):
    for j in range(n):
        if j == 0 or j==n-1 or i == n-1 or i ==0 :
            print("1 ",end="")
        else:
            print("  ",end="")
    print()

# enter a  number : 5
# 1 1 1 1 1
# 1       1
# 1       1
# 1       1
# 1 1 1 1 1
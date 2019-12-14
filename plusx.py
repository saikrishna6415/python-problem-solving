n = int(input("enter a number : "))
for i in range(n):
    for j in range(n):
        if i == n//2 or j ==n//2:
            print("X ",end="")
        else:
            print("0 ",end="")
    print()

# enter a number : 7
# 0 0 0 X 0 0 0
# 0 0 0 X 0 0 0
# 0 0 0 X 0 0 0
# X X X X X X X
# 0 0 0 X 0 0 0
# 0 0 0 X 0 0 0
# 0 0 0 X 0 0 0
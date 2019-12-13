n = int(input("enter number : "))

for  i in range(n,0,-1):
    for j in range(i,0,-1):
        print(str(j)+" ",end="")
    print()
for  i in range(n,0,-1)[::-1]:
    for j in range(i,0,-1):
        print(str(j)+" ",end="")
    print()

# output
# enter number : 5
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

n = int(input("enter number : "))

for i in range(1,n+1):
    for j in range(1,i):
        print(0,end="")
    print(i)

# enter number : 5
# 1
# 02
# 003
# 0004
# 00005

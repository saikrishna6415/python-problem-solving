n = int(input("enter a number : "))

for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end="")
    for j in range(i,n)[::-1]:
        print(j,end="")
    print()

# enter a number : 4
# 1234321
# 23432
# 343
# 4

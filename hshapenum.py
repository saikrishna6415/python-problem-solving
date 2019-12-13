n = int(input("enter a number : "))
a = [[' ' for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(i+1):
        a[i][j]= j+1

for i in range(n):
    ar=a[i][:n-1]
    print(*(a[i]+ar[::-1]) )

for i in range(n-1)[::-1]:
    ar=a[i][:n-1]
    print(*(a[i]+ar[::-1]) )


# output
# enter a number : 5
# 1               1
# 1 2           2 1
# 1 2 3       3 2 1
# 1 2 3 4   4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4   4 3 2 1
# 1 2 3       3 2 1
# 1 2           2 1
# 1               1


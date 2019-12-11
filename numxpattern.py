n = int(input("enter a number: "))

a = [[" " for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][i]=str(n-i)
        a[i][n-i-1]=str(i+1)

for i in range(n//2+1):
    print(*a[i])

for i in range(n//2+1,n):
    print(*a[i][::-1])
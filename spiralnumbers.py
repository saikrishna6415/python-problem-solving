n = int(input("enter a number : "))

a = [['' for i in range(n)]for j in range(n)]
num  = 1
i = 0
j = 0
while i>=0 and j<n:
    a[i][j]=num
    num+=1
    j+=1

i= 1
j = n-1
num = n+1
while i < n:
    a[i][j]=num
    num+=1
    i+=1

i = n-1
j = n-1
num = 2* n - 1
while j >=0:
    a[i][j]=num
    num+=1
    j-=1



for i in range(n):
    print(a[i])
n = int(input("enter a number : "))

# for i in range(1,n+1):
#     print((n-i)*(" "),end=" ")
#     k = 1
#     for  j in range(1,i+1):
#         print(str(k),end = " ")
#         k = k*(i-j)//j
#     print()
        
a = [[" " for i in range(n)]for j in range(n)]

for i in range(n+1):
    for j in range(1,i+1):
        k=1
        a[i][j]=str(k)
        k=k*(i-j)//j

for i in range(n):
    print(a[i])
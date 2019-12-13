n = int(input("enter a number : "))
 
a = [[" " for i in range(1,n+1)]for j in range(n)]

for i in range(0,n+1):
    for j in range(i,n):
        a[i][j]=i+1
        a[j][i]=i+1
            
for i in range(n):
    aa=a[i][:n-1]
    print(*(a[i]+aa[::-1]))

for i in range(n-1)[::-1]:
    aa=a[i][:n-1]
    print(*(a[i]+aa[::-1]))





# REVERSE
# n = int(input("enter a number : "))
 
# a = [[" " for i in range(1,n+1)]for j in range(n)]

# for i in range(0,n+1):
#     for j in range(i,n):
#         a[i][j]=n-i
#         a[j][i]=n-i
            
# for i in range(n):
#     aa=a[i][:n-1]
#     print(*(a[i]+aa[::-1]))

# for i in range(n-1)[::-1]:
#     aa=a[i][:n-1]
#     print(*(a[i]+aa[::-1]))



# output
# enter a number : 5
# 1 1 1 1 1 1 1 1 1
# 1 2 2 2 2 2 2 2 1
# 1 2 3 3 3 3 3 2 1
# 1 2 3 4 4 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 4 4 3 2 1
# 1 2 3 3 3 3 3 2 1
# 1 2 2 2 2 2 2 2 1
# 1 1 1 1 1 1 1 1 1



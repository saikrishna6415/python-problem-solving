n = int(input("enter a number : "))

for i in range(n):
    for j in range(i+1):
        if  j == 0 or j ==i or i ==n-1:
            print(str(j+1)+" ",end="")
        else:
            print("  ",end="")
    print()

    # OR
# arr = [[" " for i in range(n)]for j in range(n)]

# for i in range(n):
#     for j in  range(i+1):
#         if j==0 or j == i or i == n-1:
#             arr[i][j]=str(j+1)
    
# for i in range(len(arr)):
#     print(arr[i])
 
# enter a number : 5
# 1
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5


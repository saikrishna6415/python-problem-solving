n = int(input("enter a number: "))

# for i in range(n,0,-1):
#     for j in range(1,i+1,1):
#         if i == n:
#             print(j ,end=" ")
#         elif j ==1:
#             print(n-i+1,end=" ")
#         elif j==i:
#             print(n,end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")

# l = n

arr = [[" "for i in range(n+1)]for j in range(n+1)]
for i in range(n,-1,-1):
    for j in range(0,i+1,1):
        if i == n:
            arr[i][j]= str(j)
        elif j == 0:
            arr[i][j] = str(n-i)
        elif j == i:
            arr[i][j] = str(n)
        else:
            arr[i][j] = " "
        
for i in range(len(arr))[::-1]:
    print(arr[i])
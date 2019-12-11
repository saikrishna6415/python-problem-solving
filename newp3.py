n =int(input("enter a number : " ))

# for i in range(n):
#     if i ==0 or i==n-1:
#         print(" 1"*n)
#     else:
#         print(" 1"+ (n+1)*" "+"1")


for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j ==0 or j==n-1:
            print("1" ,end= " ")
        else:
            print(" " ,end=" ")
    print()
n = int(input("enter a number : "))

for  i in range(n):
    for j in range(n):
        if j == 0  or i == 0 or i ==n-1 or j == n-1:
            print("* ",end="")
        elif j ==( n-1)//2 and ( i > 0 and i < n-1):
            print(" *",end="")
        else:
            print("  ",end="")
        
    print()

            # or
# arr = [[ " "for i in range(n)]for j in range(n)]
# for  i in range(n):
#     for j in range(n):
#         if j == 0  or i == 0 or i ==n-1 or j == n-1:
#             arr[i][j]="* "
#         elif j ==( n-1)//2 and ( i > 0 and i < n-1):
#             arr[i][j]=" *"
#         else:
#             arr[i][j]="  "
# for i in range(len(arr)):
#     print(arr[i])    


# enter a number : 6
# * * * * * *
# *    *    *
# *    *    *
# *    *    *
# *    *    *
# * * * * * *

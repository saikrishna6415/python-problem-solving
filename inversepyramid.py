n = int(input("enter number : "))

for  i in range(n,0,-1):
    print((n-i)*" ",end="")
    for j in range(i,0,-1):
        print(str(n-j+1)+" ",end="")
    print()
for  i in range(n,1,-1)[::-1]:
    print((n-i)*" ",end="")
    for j in range(i,0,-1):
        print(str(n-j+1)+" ",end="")
    print()

# output
# enter number : 5
# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5
#    4 5
#   3 4 5
#  2 3 4 5
# 1 2 3 4 5

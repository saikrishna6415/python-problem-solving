n = int(input("enter number : "))

for i in range(n,0,-1):
    print((i)*" "+( str(i)+ " ")*(n-i+1))


# enter number : 4
#     4
#    3 3
#   2 2 2
#  1 1 1 1

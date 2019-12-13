n = int(input("enter a number: "))
a=1
for i in range(1,n+1):
    print(i*" ",end=" ")
    for j in range(n-i+1):
        print((str(a)+" "),end="")
        a+=(n-j)
    print()
    a=i+1


# output
# enter a number: 5
#   1 6 10 13 15
#    2 7 11 14
#     3 8 12
#      4 9
#       5

n = int(input("enter a number : "))
for  i in range(n*4):
    if i % 4 == 0:
        print(4*(" *"),end=" ")
    else:
        print(" *"+ 5*(" ") +"*",end=" ")
    print(" ")


# output
# enter a number : 3
#  * * * *
#  *     *
#  *     *
#  *     *
#  * * * *
#  *     *
#  *     *
#  *     *
#  * * * *
#  *     *
#  *     *
#  *     *
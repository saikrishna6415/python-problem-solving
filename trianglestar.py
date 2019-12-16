n = int(input("enter a number : "))

for i in range(n):
    if i == 0 :
        print(" "*(n-i)+ "* ")
    elif i ==n-1:
        print((n-i)*" " + "* "*n)
    else:
        print((n-i)*" " + "*" + (2*i-1)*" "+ "*")

        
# enter a number : 7
#        *
#       * *
#      *   *
#     *     *
#    *       *
#   *         *
#  * * * * * * *
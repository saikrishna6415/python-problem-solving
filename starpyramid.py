n = int(input("enter a number:"))
for i in range(1,2*n+1,2):
    print((2*n-i)*" "+ "* "*i)


# enter a number:7
#              *
#            * * *
#          * * * * *
#        * * * * * * *
#      * * * * * * * * *
#    * * * * * * * * * * *
#  * * * * * * * * * * * * *

for i in range(1,n+1):
    print((n-i)*" "+ "* "*i)


# enter a number:4
#    *
#   * *
#  * * *
# * * * *
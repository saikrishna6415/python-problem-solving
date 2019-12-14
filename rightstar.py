n = int(input("enter a number : "))
for i in range(1,n+1):
    print("*"*i)
for i in range(1,n)[::-1]:
    print("*"*i)


# enter a number : 4
# *
# **
# ***
# ****
# ***
# **
# *
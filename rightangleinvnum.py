n = int(input("enter number : "))

number = ""
for i in range(1,n+1):
    number+= " "+(str(i))
    print(number[::-1])

# enter number : 5
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
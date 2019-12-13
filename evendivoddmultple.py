n = int(input("enter a number : "))
while n!=1:
    if n % 2 == 0:
        n/=2
    else:
        n=3*n+1
    print(n)

# output
# enter a number : 5
# 16
# 8.0
# 4.0
# 2.0
# 1.0

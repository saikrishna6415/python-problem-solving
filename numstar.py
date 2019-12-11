n = int(input("enter number : "))

for i in range(n,0,-1):
    print((i)*" "+( str(i)+ " ")*(n-i+1))
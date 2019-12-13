n = int(input("enter number : "))

a=1
for i in range(n):
    for j in range(i+1):
        print(a%2,end="")
        a+=1
    print()


# enter number : 5
# 1
# 01
# 010
# 1010
# 10101
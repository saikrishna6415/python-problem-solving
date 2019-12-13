n = int(input("enter number : "))


number = ""
for i in range(n,0,-1):
    number+=str(i)
    print(number[::-1])


# enter number : 5
# 5
# 45
# 345
# 2345
# 12345

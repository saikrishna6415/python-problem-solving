n = int(input("enter number : "))


number = ""
for i in range(n,0,-1):
    number+=str(i)
    print(number[::-1])
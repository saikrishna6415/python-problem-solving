n = int(input("enter number : "))


number = ""
for i in range(1,n+1):
    number+=str(i)
    print(number[::-1])

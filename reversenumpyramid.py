n = int(input("enter number : "))

number = ""
for i in range(1,n+1):
    number+=(" "+str(i))
    string=((n-i)*" "+number)

for i in range(0,len(string)+2,2)[::-1]:
    print((len(string)-i)//2*" "+string[:i])
            
            # OR

for i in range(1,n+1)[::-1]:
    print((n-i)*" ",end=" ")
    for j in range(1,i+1):
        print(str(j)+" ",end="")
    print()


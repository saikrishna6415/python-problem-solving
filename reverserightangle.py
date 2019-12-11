n = int(input("enter number : "))

number = ""
for i in range(1,n+1):
    number+=(" "+str(i))
    string=((n-i)*" "+number)

for i in range(0,len(string)+2,2)[::-1]:
    print(string[:i])
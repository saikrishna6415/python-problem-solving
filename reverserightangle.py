n = int(input("enter number : "))

number = ""
for i in range(1,n+1):
    number+=(" "+str(i))
    string=((n-i)*" "+number)

for i in range(0,len(string)+2,2)[::-1]:
    print(string[:i])


# enter number : 5
#  1 2 3 4 5
#  1 2 3 4
#  1 2 3
#  1 2
#  1

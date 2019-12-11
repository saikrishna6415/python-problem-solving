string = input("enter a string : ")
for i in range(len(string)):
    print(string[:i])
for i in range(len(string)+1)[::-1]:
    print(string[:i])
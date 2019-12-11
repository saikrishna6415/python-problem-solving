s = input("enter a string : ")
s=s.strip()
s1=s.split(" ")

l= len(max(s1, key=len))
a = [[" " for x in range(len(s1))] for y in range(l)]  
for i in range(len(s1)):
    for j in range(len(s1[i])):
        a[j][i]=s1[i][j]
        
for i in range(l):
    print(a[i])
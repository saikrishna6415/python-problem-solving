n=int(input())
l=n*2
a = [[" " for x in range(l)] for y in range(l)] 
for j in range(len(a)):
    a[j][j]="*"
    a[j][len(a)-j-1]="*"

for i in range(len(a)):
    print(a[i])

# for i in range(n):
#     print((i+2)*" " + "*"+ (n-2)*" "+ " "*i) 

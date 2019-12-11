n = int(input("enter number : "))

a = [[" "for i in range(n+1)]for i in range(n+1)]
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if j ==1 or j ==i or i ==n:
            a[i][j] = 1
        else:
            a[i][j]=" "

for i in range(1,n+1):
    print(*a[i])
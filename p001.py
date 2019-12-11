n = int(input())
l = 5 
a = [[" " for i in range(l)]for  j in range(l)]

for row in range(len(a)):
    for col in range(len(a)):
        if row ==0 and col in {0,4} :
            a[row][col]="*"
        if row ==1 and col in {1,3} :
            a[row][col]="*"
        if row ==2 and col ==2:
            a[row][col]="*"
        if row ==3 and col in {1,3} :
            a[row][col]="*"
        if row ==4 and col in {0,4} :
            a[row][col]="*"
            



for j in range(n):
    for  i in range(len(a)):
        print(a[i])
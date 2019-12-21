n = int(input("enter a number : "))
 
arr = [[" "for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(i+1):
        arr[i][j]="*"

for i in range(len(arr))[::-1]:
    print(*(arr[i]+ arr[i][::-1]))
for i in range(len(arr)):
    print(*(arr[i]+ arr[i][::-1]))
    
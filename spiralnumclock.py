n = int(input("enter a number : "))
arr = [[" " for i in range(n)]for j in range(n)]
nstart = 1
low = 0
high = n-1
for i in range(n+1//2):
    for j in range(low,high+1):
        arr[i][j]=nstart
        nstart+=1
    for j in range(low+1,high+1):
        arr[j][high]=nstart
        nstart+=1
    for j in range(high-1,low-1,-1):
        arr[high][j]=nstart
        nstart+=1
    for j in range(high-1,low,-1):
        arr[j][low]=nstart
        nstart+=1
    low+=1
    high-=1

for i in range(len(arr)):
    print(*arr[i])

# enter a number : 5
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9




nstart = n**2
low = 0
high = n-1
for i in range(n+1//2):
    for j in range(low,high+1):
        arr[i][j]=nstart
        nstart-=1
    for j in range(low+1,high+1):
        arr[j][high]=nstart
        nstart-=1
    for j in range(high-1,low-1,-1):
        arr[high][j]=nstart
        nstart-=1
    for j in range(high-1,low,-1):
        arr[j][low]=nstart
        nstart-=1
    low+=1
    high-=1

for i in range(len(arr)):
    print(*arr[i])              #arr[i][::-1] for clockwise spiral

# enter a number : 4
# 16 15 14 13
# 5 4 3 12
# 6 1 2 11
# 7 8 9 10
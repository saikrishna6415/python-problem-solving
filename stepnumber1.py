arr = list(input("enter a number : ")) 

for i in range(len(arr)):
    arr[i]=int(arr[i])


if arr[len(arr)-2]-arr[len(arr)-1] != 1:
    print("NO")
else:
    print("YES")

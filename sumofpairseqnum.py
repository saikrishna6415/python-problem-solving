arr = [1,3,2,3,8,9,5,4,8,10]
number = 6
arr2 = [ ]
k=0
for j in range(len(arr)):
    for i in range(len(arr)):
        if arr[k] + arr[i]==number:
            arr2.append((arr[k],arr[i]))
    k+=1

print(list(set(arr2)))

# [(5, 1), (3, 3), (1, 5), (4, 2), (2, 4)]
# removing duplicates using set
arr = [121,234,43,34,343,121,33,22,23,44,44,23,433,121,43,23]
arr1 = set(arr)
arr1 = list(arr1)

# couting duplicates using for loop 0(n**2)
arr2 = [ ]
for i in range(len(arr)):
    count = 0
    for j in range(1,len(arr)):
        if  arr[i]==arr[j]:
            count+=1
    arr2.append(count)
dict1 = { }
for i in range(len(arr)):
    dict1[arr[i]] = arr2[i]
arr3 = set(arr)
print(arr2)
print(dict1)
print(arr3)

# [2, 1, 2, 1, 1, 2, 1, 1, 3, 2, 2, 3, 1, 2, 2, 3]
# {121: 2, 234: 1, 43: 2, 34: 1, 343: 1, 33: 1, 22: 1, 23: 3, 44: 2, 433: 1}
# {33, 34, 234, 43, 44, 433, 23, 22, 343, 121}



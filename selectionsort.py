def selection_sort(arr):
    for i in range(len(arr)):
        element = i 
        for j in range(i+1,len(arr)):
            if arr[element] > arr[j]:
                element = j
            arr[i],arr[element] = arr[element],arr[i]
arr = [19,2,31,45,30,11,121,27]
selection_sort(arr)
print(arr)

# [2, 11, 19, 27, 30, 31, 45, 121]
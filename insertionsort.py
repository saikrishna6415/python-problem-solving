def insertionSort(arr):
    for i in range(1,len(arr)):
        currentvalue = arr[i]
        position = i 
        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position-1]
            position= position-1
        arr[position] = currentvalue

arr = [19,2,31,45,30,11,121,27]
insertionSort(arr)
print(arr)
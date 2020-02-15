# arr = [5,4,4,2,2,8]
# i = 0 
# arr1 = [ ]
# arr.sort()
# while i < len(arr):
#     arr1.append(len(arr)-i)
#     while arr[i]==arr[i+1]:
#         i+=1
#     i+=1
# print(arr1)
# a = [[1,2,3,4],
#     [5],
#     [6,7],
#     [8],
#     [9,10,11]
# ]

# for i in range(len(a))[::-1]:
#     a[i]= a[i][::-1]
#     print(a[i])

arr = [ [-9,-9,-9,1,1,1],
        [0,-9,0,4,3,2],
        [-9,-9,-9,1,2,3],
        [0,0,8,6,6,0],
        [0,0,0,-2,0,0],
        [0,0,1,2,4,0]]
li=[]
for i in range(len(arr)-2):
    for j in range(len(arr)-2):
        li.append(sum(arr[i][j:j+3]+arr[i+2][j:j+3])+arr[i+1][j+1])
        

print(max(li))
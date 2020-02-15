scores = [100,100,50,40,40,20,10]
alice = [5,25,50,120]

# arr = [ ]
# arr1 = []
# for i in range(len(alice)):
#     arr1.append(alice[i])
#     arr.append(scores+arr1)
# arr2 = scores+alice
# arr2 = set(arr2)
# arr2= list(arr2)
# # arr2 = arr2.sort()
# for  i in range(len(arr)):
#     arr[i].sort(reverse=True)
#     print(arr[i])
# print(arr2)


scores = sorted(list(set(scores)))
index = 0
rank_list = []
n = len(scores)
for i in alice:
    while (n > index and i >= scores[index]):
        index += 1
    rank_list.append(n+1-index)
    print(rank_list)
print(rank_list)
    
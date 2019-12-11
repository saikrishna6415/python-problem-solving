m = 3
n= m*2
arr=[]
for i in range(n):
 if i < m+m:
   if i< m:
     arr.append([])
     for j in range(i):
       arr[i].append(' ')
     arr[i].append('*')
     for k in range(m-1-i):
       arr[i].append(' ')
     for k in range(m-1-i):
       arr[i].append(' ')
     arr[i].append('*')
     for j in range(i):
       arr[i].append(' ')
   if i >= m:
     arr.append(arr[m+m-i-1].copy())
#  if i >= m+m:
#    arr.append(arr[n-i-1].copy())
for i in range(len(arr)):
 print(arr[i])
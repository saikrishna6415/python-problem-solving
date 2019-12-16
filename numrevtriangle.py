n = int(input("enter a number :"))

for i in range(1,n+1):
    print((n-i)*" ",end="")
    k=i
    for j in range(1,i+1):
        print(k,end="")
        k+=1
    k =i-2
    for j in range(1,i):
        print(str(i+k),end="")
        k-=1
   
    print()

# enter a number :5
#     1
#    232
#   34543
#  4567654
# 567898765

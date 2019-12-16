n = int(input("enter a number : "))

for i in range(n)[::-1]:
    if i % 2 ==0:
        for j in range(i//2+1):
            print(chr(65+j)+"",end=" ")
    else:
        for j in range(i//2+1):
            print(" "+chr(90-j),end="")
    print()

for i in range(1,n):
    if i % 2 ==0:
        for j in range(i//2+1):
            print(chr(65+j)+"",end=" ")
    else:
        for j in range(i//2+1):
            print(" "+chr(90-j),end="")
    print()



# enter a number : 8
#  Z Y X W
# A B C D
#  Z Y X
# A B C
#  Z Y
# A B
#  Z
# A
#  Z
# A B
#  Z Y
# A B C
#  Z Y X
# A B C D
#  Z Y X W
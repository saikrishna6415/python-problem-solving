n = int(input("enter a number : "))
A = 65
Z = 90
for i in range(1,n+1):
    if i % 2 !=0:
        for j in range(1,i+1):
            print(chr(A),end=" ")
            A+=1
        print()
    else:
        print("<",end="")
        for j in range(1,i+1):
            print(chr(Z),end=" ")
            Z-=1

        print()

    
# enter a number : 5
# A
# <Z Y
# B C D
# <X W V U
# E F G H I

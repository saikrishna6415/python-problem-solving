n = int(input("enter number : "))

for i in range(1,n+1):
    if i % 2==0:
        print("$ ",end="")
    else:
        print(str(i)+" ",end="")

# enter number : 6
# 1 $ 3 $ 5 $
n = int(input("enter a number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*"+str(j),end="")
    print()
for i in range(1,n)[::-1]:
    for j in range(1,i+1):
        print("*"+str(j),end="")
    print()

# enter a number : 5
# *1
# *1*2
# *1*2*3
# *1*2*3*4
# *1*2*3*4*5
# *1*2*3*4
# *1*2*3
# *1*2
# *1

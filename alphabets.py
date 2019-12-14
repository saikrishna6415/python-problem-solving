n = int(input("enter a number : "))

for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()

# enter a number : 4
# A
# AB
# ABC
# ABCD


for i in range(n):
    for j in range(i+1):
        print(chr(97+j),end="")
    print()

# enter a number : 4
# a
# ab
# abc
# abcd
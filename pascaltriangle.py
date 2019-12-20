n = int(input("Enter a number : "))
for i in range(0, n):
    k = 1
    print((n-i)*" ",end=" ")
    for j in range(0, i+1):
        print(str(k)+ " " ,end="")
        k = int(k * (i - j) / (j + 1))
    print()
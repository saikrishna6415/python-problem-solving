s = input("enter a string : ")
n = int(input("enter number : "))
if n==1:
    print(s)
l=len(s)
row = 0
a = [[" " for x in range(l)] for y in range(l)]  

for i in range(l): 
        a[row][i] = s[i]
      
        if row == n - 1: 
            down = False    
        elif row == 0: 
            down = True
        if down == True: 
            row = row + 1
        else: 
            row = row - 1  

for i in range(n):
    print(a[i])

# output
# enter a string : saikrishna
# enter number : 3
# ['s', ' ', ' ', ' ', 'r', ' ', ' ', ' ', 'n', ' ']
# [' ', 'a', ' ', 'k', ' ', 'i', ' ', 'h', ' ', 'a']
# [' ', ' ', 'i', ' ', ' ', ' ', 's', ' ', ' ', ' ']
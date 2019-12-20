# s = input("enter a string : ")
# print(s[::-1])

# #  or 
# s1 =[ ]
# s = list(s)
# for i in range(len(s)-1,-1,-1):
#     s1.append(s[-i])
    
# print("".join(s1))

# s = "abcd"
# s2 ="abcd"``
# s =list(s)
# s2 =list(s2)
# if s.sort() == s2.sort():
#     print("is anagaram")





# s = "saikrishna"
# s1 = set(s)
# s1 = list(s1)
# s1.sort()
# s2 = [ ]
# for i in range(len(s1)):
#     s2.append(s.count(s1[i]))
# s3 =[ ]
# for i in range(len(s2)):
#     s3.append(str(s2[i])+s1[i])
# print("".join(s3))




# s = "sai krishna kotagiri"
# s = s.split(" ")
# print("".join(s))



# s = "saikrishna"
# s = list(s)
# s1 = []
# for i in range(len(s)):
#     s1.append(s.count(s[i]))
# for i in range(len(s)):
#     if s1[i]<=1:
#         print(s[i])
#         break
# print(s1)




# s = "123ac45"
# s1 = []

# for i in range(len(s)):
#     if not ((s[i]>='a' and s[i]<= 'z') or (s[i]>='A' and s[i]<='Z')):
#         s1.append("yes")
# if ["yes"]*len(s) == s1 :
#     print("yes")
# else:
#     print("No")


# s = "sai krishna kotagiri"
# print(s[::-1])


# s = "sai krishna kotagiri"
# s = s[::-1].split(" ")
# print(" ".join(s[::-1]))

# s = "sai krishna kotagiri"
# s = s.split(" ")
# print(s[::-1])


# string=input("Enter a string to count vowels:")
# vowels = 0
# consonants=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
#       elif i != " ":
#         consonants+=1
# print("No.ofvowels:"+ str(vowels))
# print("No.of consonants :"+ str(consonants))





# from itertools import permutations
# print([''.join(p)for p in permutations('sai')])




# def permute(data, i, length): 
#     if i==length: 
#         print(''.join(data) )
#     else: 
#         for j in range(i,length): 
#             #swap
#             data[i], data[j] = data[j], data[i] 
#             permute(data, i+1, length) 
#             data[i], data[j] = data[j], data[i]  
# string = "SAI"
# n = len(string) 
# data = list(string) 
# permute(data, 0, n)



# s = "saikrishna"
# s1 = list(s)
# s2 = sorted(s1)
# print("".join(s2))


# n = 1221
# n1 = str(n)
# n1 = list(n1)
# print(n1)
# mid = len(n1)//2
# if n1[:mid] == n1[mid:][::-1]:
#     print("Yes is is a palindrome")
#         # OR
# if n1 == n1[::-1]:
#     print("Palindrome")




s = "forgeeksskeegfor"
s1 = [ ]
for i in range(len(s)//2):
    if s[i] == s[-i]:
        s1.append(s)
print(s1)




# def isSafe (board, row, col):
#     # check left row
#     for y in range(col):
#         if board[row][y] == 1:
#             return False
#     # check diagonal left top
#     for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[x][y] == 1:
#             return False
#     # check diagonal left bottom
#     for x, y in zip(range(row, N, 1), range(col, -1, -1)):
#         print(board[x][y],end=" ")
#         if board[x][y] == 1:
#             return False

#     return True

# def generateSolution(board, col):
#     # terminating condition
#     # all columns covered
#     global N
#     if col >= N:
#         return True
#     # loop over all the rows
#     for i in range(N):
#         if isSafe(board, i, col) == True:
#             board[i][col] = 1
#             # recursively place other queens
#             if generateSolution(board, col + 1) == True:
#                 return True
#             # unmark queen spot
#             board[i][col] = 0
#     # backtrack
#     return False


# N = int(input(("enter chess board size: ")))
# startCol = 0
# board = [[0 for i in range(N)] for j in range(N)]
# # print(board)

# if generateSolution(board, startCol) == False:
#     print("No Solution Exists")
# else:
#     print("Solution exists")
#     for i in board:
#         print(i)




# def generatesolution(board,col):
#     global N
#     if col >= N:
#         return True
#     for i in range(N):
#         if isSafe(board,i,col)==True:
#             board[i][col]=1
#             if generatesolution(board,col+1)==True:
#                 return True
#             board[i][col]=0


# def isSafe(board,row,col):
#     for i in range(col):
#         if board[row][i]==1:
#             return False
#     for x, y in zip(range(row,-1,-1),range(col,-1,-1)):
#         if board[x][y]==1:
#             return False
#     for x,y in zip(range(row,N,-1),range(col,-1,-1)):
#         if board[x][y]==1:
#             return False
#     return True
# N = 4
# startcol = 0
# board = [[0 for i in range(N)]for j in range(N)]

# if generatesolution(board,startcol)==False:
#     print("No soluton")
# else:
#     print("solution exists")
#     for i in board:
#         print(i)









# def queenpuzzle(rows,columns):
#     if rows <= 0:
#         return [[]]
#     else:
#         return addqueen(rows-1,columns)

# def addqueen(newrow,columns):
#     newsol = []
#     prev = queenpuzzle(newrow,columns)
#     for i in range(len(prev)):
#         sol = prev[i]
#         for newcol in range(columns):
#             if not hasconflict(newrow,newcol,sol):
#                 newsol.append(sol +( [newcol]))
#     return sol

# def hasconflict(newrow,newcol,sol):
#     for i in range(newrow):
#         if sol[i] == newcol or sol[i+1] == newcol + newrow or sol[i-1] ==newcol-newrow:
#             return True
#     return False
# print(queenpuzzle(8,8))
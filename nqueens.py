# global N 
# N = int(input("enter board size : " ))
  
# def printSolution(board): 
#     for i in range(N): 
#         for j in range(N): 
#             print (board[i][j], end = " ") 
#         print() 
# def isSafe(board, row, col): 
#     for i in range(col): 
#         if board[row][i] == 1: 
#             return False 
#     for i, j in zip(range(row, -1, -1),  
#                     range(col, -1, -1)): 
#         if board[i][j] == 1: 
#             return False
#     for i, j in zip(range(row, N, 1),  
#                     range(col, -1, -1)): 
#         if board[i][j] == 1: 
#             return False
  
#     return True
  
# def solveNQUtil(board, col):  
#     if col >= N: 
#         return True
#     for i in range(N): 
  
#         if isSafe(board, i, col): 
#             board[i][col] = 1
#             if solveNQUtil(board, col + 1) == True: 
#                 return True
#             board[i][col] = "."
#     return False
# def solveNQ(): 
#     board =[ ["." for i in range(N) ]for j in range(N)] 
  
#     if solveNQUtil(board, 0) == False: 
#         print ("Solution does not exist") 
#         return False
  
#     printSolution(board) 
#     return True

# solveNQ() 
  



#   IInd METHOD
class GfG: 
    def __init__(self): 
        self.MAX = 10
        self.arr = [0] * self.MAX
        self.no = 0
  
    def breakLine(self): 
        print("\n------------------------------------------------") 
  
    def canPlace(self, k, i): 
          
        # Helper Function to check  
        # if queen can be placed  
        for j in range(1, k): 
            if (self.arr[j] == i or 
               (abs(self.arr[j] - i) == abs(j - k))): 
                return False
        return True
  
    def display(self, n): 
          
        # Function to display placed queen 
        self.breakLine() 
        self.no += 1
        print("Arrangement No.", self.no, end = " ") 
        self.breakLine() 
  
        for i in range(1, n + 1): 
            for j in range(1, n + 1): 
                if self.arr[i] != j: 
                    print("\t_", end = " ") 
                else: 
                    print("\tQ", end = " ") 
            print() 
  
        self.breakLine() 
  
    def nQueens(self, k, n): 
          
        # Function to check queens placement 
        for i in range(1, n + 1): 
            if self.canPlace(k, i): 
                self.arr[k] = i 
                if k == n: 
                    self.display(n) 
                else: 
                    self.nQueens(k + 1, n) 
  
# Driver Code 
if __name__ == '__main__': 
    n = 4
    obj = GfG() 
    obj.nQueens(1,n) 
  
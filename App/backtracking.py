# board = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,0,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,0,9,0,0,5],
#     [0,0,0,2,8,0,0,7,0],
# ]

# # board = [
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# #     [0,0,0,0,0,0,0,0,0],
# # ]
# # Check if a num can be placed in pos

# def valid(num, row, column,board):
#     # Check row
#     for i in board[row]:       # Checks the values of the row
#         if i == num:
#             return False

#     # Check column
#     for i in board:
#         if i[column] == num:        # Checks every row then the column index
#             return False

#     # Check Square
#     box_x = (row//3) * 3            # (* 3 )- To get the coordinates back
#     box_y = (column//3) * 3

#     for i in range(0,3):
#         for j in range(0,3):
#             #print(board[box_x + i][box_y + j], num)
#             if board[box_x + i][box_y + j] == num:
#                 return False           

#     #print('Valid')
#     return True

# def displayBoard(board):
#     for i in range(9):      
#         line = ''
#         if (i == 3) or(i == 6):         # Prints the line break
#             print('---------------')     


#         for j in range(9):
#             if (j == 2) or (j==5):          # Adds the Num and separator
#                 line += str(board[i][j]) + ' | '

#             else: 
#                 line += str(board[i][j])
#         print(line)
#     print('\n______Break______')
    


# # Find the unsolved slots
# def emptySquare(board):
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 0:
#                 return i,j          # Row column


# displayBoard(board)
# valid(board, 9, (8,7))

# row,column = emptySquare(board)
# print(row,column)

# def solve(board):
#     if emptySquare(board): 
#         row,column = emptySquare(board)              
#         for i in range(1,10):       # Loops through 1 to 9 for the inputs
#             if valid(i,row,column,board):     
#                 #print(f'{i} is valid at ({row},{column})')
#                 board[row][column] = i
#                 solve(board)
#                 board[row][column] = 0
#         return              
#     displayBoard(board)

# print((solve(board)))

# #
# def solve(board):
#     for y in range(9):
#         for x in range(9):
#             if board[y][x] == 0:
#                 for n in range(1,10):
#                     if possible(board,y,x,n):
#                         board[y][x] = n
#                         solve(board)
#                         board[y][x] = 0
#                 return
#     return (board)

# def possible(board,y,x,n):
#     for i in range(0,9):
#         if board[y][i] == n:
#             return False
#     for i in range(0,9):
#         if board[i][x] == n:
#             return False
    
#     x0 = (x//3)*3
#     y0 = (y//3)*3
#     for i in range(0,3):
#         for j in range(0,3):
#             if board[y0+i][x0+j] == n:
#                 return False
            
#     return True

# solve(board)
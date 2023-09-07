board =[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,0,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,0,9,0,0,5],
    [0,0,0,2,0,0,0,0,0],
]

def solve_sudoku(board):

    def is_valid(row, col, num):
        # Check if the number is not present in the same row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        # Check if the number is not present in the same 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    def backtrack():
        empty_cell = find_empty_cell()
        if not empty_cell:
            return True  # All cells are filled, puzzle solved
        
        row, col = empty_cell
        for num in range(1, 10):
            if is_valid(row, col, num):
                board[row][col] = num
                
                if backtrack():
                    return True  # Continue solving with the current number
                
                board[row][col] = 0  # Backtrack if the current number doesn't lead to a solution
                
        return False  # No valid number found, need to backtrack
    
    def find_empty_cell():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    if backtrack():
        return board
    
    else:
        return ('Invalid Puzzle')  # No solution exists

answer = (solve_sudoku(board))
for row in answer:
    print(row)
def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    n = len(board)
    
    # If all queens are placed, return True
    if col >= n:
        return True

    # Try placing a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1):
                return True

            board[row][col] = 0  # Backtrack if placing queen didn't work

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

def n_queens_with_initial_queen(n, initial_row, initial_col):
    # Initialize the board with 0s
    board = [[0] * n for _ in range(n)]
    
    # Place the first queen at the specified initial position
    board[initial_row][initial_col] = 1

    # Start placing the remaining queens from column 1
    if solve_n_queens(board, 1):
        print("\nSolution:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    # Get board size and initial position from the user
    n = int(input("Enter the number of queens (board size): "))
    row = int(input(f"Enter the row (0 to {n-1}) for the first queen: "))
    col = int(input(f"Enter the column (0 to {n-1}) for the first queen: "))

    # Ensure the initial position is within the board limits
    if 0 <= row < n and 0 <= col < n:
        n_queens_with_initial_queen(n, row, col)
    else:
        print("Invalid position!")
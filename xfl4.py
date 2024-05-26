def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, n):
    """Utilize backtracking to solve the N-Queen problem."""
    # Base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_nq_util(board, col + 1, n):
                return True

            board[i][col] = 0  # backtrack

    return False

def solve_nq(n):
    """Solve the N-Queen problem and print the solution."""
    board = [[0] * n for _ in range(n)]

    if not solve_nq_util(board, 0, n):
        print("Solution does not exist")
        return False

    print_board(board, n)
    return True

def print_board(board, n):
    """Print the board configuration."""
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Solve the 4-Queen problem
print("4-Queen Problem Solution:")
solve_nq(4)

print("\n8-Queen Problem Solution:")
# Solve the 8-Queen problem
solve_nq(8)

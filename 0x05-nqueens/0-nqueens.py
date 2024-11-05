#!/usr/bin/python3
"""import statement"""
import sys

def print_solution(board):
    """Prints the board solution in the required format"""
    solution = []
    for col in range(len(board)):
        solution.append([col, board[col]])
    print(solution)

def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(board, col, N):
    """Recursive function to solve the N queens problem"""
    if col == N:
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(board, col + 1, N)

def main():
    """Main function to parse arguments and start the solving process"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print usage information and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    """Print an error message and exit with status 1."""
    print(message)
    sys.exit(1)


def is_safe(board, row, col):
    """
    Check if placing a queen at board[row] = col is safe.

    Args:
        board (list): The board state with column positions of queens.
        row (int): The current row to check.
        col (int): The column to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col:
            return False

    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueens(board, row, n):
    """
    Solve the N Queens problem using backtracking.

    Args:
        board (list): The board state with column positions of queens.
        row (int): The current row being processed.
        n (int): The size of the board (N).
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def main():
    """Main function to handle user input and start the solving process."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if n < 4:
        print_error_and_exit("N must be at least 4")

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()

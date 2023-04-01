from math import ceil


def print_board(board):
    print("========== Connect4 =========\nPlayer 1: X       Player 2: O\n\n  1   2   3   4   5   6   7")
    for i in range(len(board)):
        print(" --- --- --- --- --- --- ---")
        row = ""
        for j in range(len(board[i])):
            column_str = "| "
            if (board[i][j] == 0):
                column_str += "  "
            elif (board[i][j] == 1):
                column_str += "X "
            else:
                column_str += "O "
            row += column_str
        print(row + "|")
    print(" --- --- --- --- --- --- ---\n=============================")


def create_board(x, y):
    return [[0 for _ in range(x)] for _ in range(y)]

    return create_board


if __name__ == "__main__":
    # Enter test code below
    board = create_board(10, 12)
    print_board(board)
    # print(ceil(5/2))

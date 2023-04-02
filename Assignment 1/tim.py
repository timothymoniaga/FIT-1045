# from cgi import test
from cgi import test
from math import ceil
import random
import copy


def validate_input(prompt, valid_inputs):
    while True:
        userInput = str(input(prompt))
        if (userInput in valid_inputs):
            return userInput
        else:
            print("Invalid input, please try again.")


def create_board():
    return [[0 for _ in range(7)] for _ in range(6)]


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


def drop_piece(board, player, column):
    column = int(column)
    i = len(board) - 1
    while i >= 0:
        if (board[i][column-1] == 0):
            board[i][column-1] = player
            return True
        i -= 1
    return False


def remove_piece(board, column):
    column = int(column)
    for i in range(len(board)):
        if (board[i][column - 1] != 0):
            board[i][column - 1] = 0


def get_row(board, column):
    column = int(column)
    for i in range(len(board)):
        if (board[i][column - 1] != 0):
            return i
    return 0


def execute_player_turn(player, board):  # Task 5
    while True:
        column = validate_input(
            "Player " + str(player) + ", please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5", "6", "7"])
        if (drop_piece(board, player, column)):
            return int(column)
        else:
            print("That column is full, please try again.")


def end_of_game(board):
  # TODO: check for wins diagonal = 1/2. Game is not over = 0. Game is a draw = 3
  # dict key value stuff: {key: [player number, column index, row index]}
    outer_index_counter = len(board) - 1
    stored_values = {}
    key_index = 0
    while (outer_index_counter >= 0):
        inner_index_counter = len(board[outer_index_counter]) - 1
        while (inner_index_counter >= 0):
            if (board[outer_index_counter][inner_index_counter] != 0):
                stored_values[key_index] = [board[outer_index_counter][inner_index_counter],
                                            inner_index_counter+1,
                                            outer_index_counter+1]
                key_index += 1
            inner_index_counter -= 1
        outer_index_counter -= 1

    total_num_elements = sum(len(inner_list) for inner_list in board)

    # print(count_connected_horizontal(stored_values, 1))
    # print(len(board) * len(board[0]))
    diagonal_win = check_diagonal_win(board)
    horizontal_win = check_horizontal_win(stored_values)
    vertical_win = check_vertical_win(stored_values)

    if (horizontal_win != 0):
        return (horizontal_win)
    elif (vertical_win != 0):
        return (vertical_win)
    elif (diagonal_win != 0):
        return (diagonal_win)
    elif (len(stored_values) >= total_num_elements):
        return 3
    else:
        return 0


def check_horizontal_win(stored_values):
    for key, value in stored_values.items():

        # print(stored_values.get(key, [0][1]))
        if (value[0] == stored_values.get(key+1, [0])[0] == stored_values.get(key+2, [0])[0] == stored_values.get(key+3, [0])[0]
                and value[2] == stored_values.get(key+1, [2])[2] == stored_values.get(key+2, [2])[2] == stored_values.get(key+3, [2])[2]
                and value[1] == stored_values.get(key+1, [1])[1] + 1 == stored_values.get(key+2, [1])[1] + 2 == stored_values.get(key+3, [1])[1] + 3):
            return value[0]
    return 0


# def test_horizontal_count(stored_values, player):
#     max_count = 0
#     for i in range(1, 7):
#         for key, value in stored_values.items():
#             if stored_values.get(key)

def count_connected(board, row, col, player):
    """Counts the number of connected pieces of a player in a given direction"""
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != player:
        return 0
    count = 1

    # search in each direction (vertical, horizontal, diagonal)
    for drow, dcol in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        r, c = row + drow, col + dcol
        while r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == player:
            count += 1
            r += drow
            c += dcol

    return count


# def count_connected_horizontal(stored_values, player):
#     # Iterate through each row and check for consecutive tokens of player's number
#     connected_count = 0
#     for row in range(1, 7):
#         for col in range(1, 8-3):
#             if all(stored_values[key][0] == player for key in stored_values
#                    if stored_values[key][1] == col+i and stored_values[key][2] == row):
#                 connected_count += 1
#     return connected_count


def check_vertical_win(stored_values):
    sorted_dict = dict(sorted(stored_values.items(), key=lambda x: x[1][1]))
    values = list(sorted_dict.values())

    for i in range(len(values)-3):

        if (values[i][1] == values[i+1][1] == values[i+2][1] == values[i+3][1]) and \
                (values[i][0] == values[i+1][0] == values[i+2][0] == values[i+3][0]):
            return (values[i][0])
    return 0


def check_diagonal_win(board):
    # Check for diagonal wins foward slash /
    for i in range(len(board) - 3):
        for j in range(len(board[i]) - 3):
            if (board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]) and board[i][j] != 0:
                return board[i][j]

    # Check for diagonal wins back slash \
    for i in range(len(board) - 3):
        for j in range(3, len(board[i])):
            if (board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]) and board[i][j] != 0:
                return board[i][j]

    return 0


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def local_2_player_game():
    board = create_board()
    count = 0
    win = 0
    previous_turn = 0
    while win == 0:
        clear_screen()
        print_board(board)
        if (count >= 1):
            print("Player " + str((((count - 1) % 2) + 1)) +
                  " dropped a piece into column " + str(previous_turn))

        previous_turn = execute_player_turn((count % 2) + 1, board)

        if (count >= 6):
            win = end_of_game(board)
        count += 1
        print(win)

    print_board(board)
    print("Player " + str(win) + " has won!")
    input("Press return/enter to continue...")


def print_main_menu():
    print("=============== Main Menu ===============")
    print("Welcome to Connect 4!")
    print("1. View Rules")
    print("2. Play a local 2 player game")
    print("3. Play a game against the computer")
    print("4. Exit")
    print("=========================================")


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def main():
    user_input = ""
    while user_input != "4":
        print_main_menu()
        user_input = validate_input(
            "Select an option 1-4: ", ["1", "2", "3", "4"])
        if (user_input == "1"):
            print_rules()
            input("Press return/enter to continue...")
        elif (user_input == "2"):
            local_2_player_game()
        elif (user_input == "3"):
            game_against_cpu()  # does not work
        else:
            return

        clear_screen()


def game_against_cpu():
    raise NotImplementedError


def cpu_player_easy(board, player):
    indices = [i + 1 for i, element in enumerate(board[0]) if element == 0]
    rand_num = random.choice(indices)
    drop_piece(board, player, rand_num)
    return rand_num


def cpu_player_medium(board, player):
    temp_board = copy.deepcopy(board)
    enemy_player = 2 if player == 1 else 1

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, player, i):
            if (end_of_game(temp_board) != 0):
                drop_piece(board, player, i)
                return i

    temp_board = copy.deepcopy(board)

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, enemy_player, i):
            if (end_of_game(temp_board) != 0):
                drop_piece(board, player, i)
                return i

    indices = [i + 1 for i, element in enumerate(board[0]) if element == 0]
    rand_num = random.choice(indices)
    drop_piece(board, player, rand_num)
    # print_board(board)
    return rand_num


def cpu_player_hard(board, player):
    temp_board = copy.deepcopy(board)
    enemy_player = 2 if player == 1 else 1

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, player, i):
            if (end_of_game(temp_board) != 0):
                drop_piece(board, player, i)
                return i
        remove_piece(temp_board, i)

    # temp_board = copy.deepcopy(board)

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, enemy_player, i):
            if (end_of_game(temp_board) != 0):
                drop_piece(board, player, i)
                return i
        remove_piece(temp_board, i)

    # temp_board = copy.deepcopy(board)

    best_move = None
    max_count = 0
    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, player, i):
            row = get_row(temp_board, i)
            count = count_connected(temp_board, row, i, player)
            if count > max_count:
                best_move = i
                max_count = count
            remove_piece(temp_board, i)

    if best_move is not None:
        drop_piece(board, player, best_move)
        return best_move

    indices = [i + 1 for i, element in enumerate(board[0]) if element == 0]
    sorted_indicies = sorted(
        indices, key=lambda x: get_distance_from_target(x, target=(ceil(len(board[0])/2))))
    # rand_num = random.choice(indices)
    print(sorted_indicies)
    drop_piece(board, player, sorted_indicies[0])
    # print_board(board)
    return sorted_indicies[0]


def get_distance_from_target(num, target):
    return abs(target - num)


if __name__ == "__main__":
    # board = create_board()
    # print(len(board[0]))

    # indices = [i + 1 for i, element in enumerate(board[0]) if element == 0]

    # print(indices)
    # print(random.choice(indices))

    # validate_input("Select an option 1-4: ", [1, 2, 3, 4])
    # print_board(board)
    # print(end_of_game(board))
    # local_2_player_game()
    # main()
    # end_of_game(board)
    outcome = cpu_player_hard(board, 1)
    print(outcome)
    # cpu_player_easy(board, 1)

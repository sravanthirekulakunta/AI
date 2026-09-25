import random

def display(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, player):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for w in wins:
        if board[w[0]] == player and board[w[1]] == player and board[w[2]] == player:
            return True

    return False


def ai_move(board):
    empty = []

    for i in range(9):
        if board[i] not in ["X", "O"]:
            empty.append(i)

    if empty:
        position = random.choice(empty)
        board[position] = "O"


board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

print("TIC TAC TOE")
print("You = X")
print("AI Robot = O")

while True:

    display(board)

    # Human move
    choice = int(input("Enter your position (1-9): "))

    if choice < 1 or choice > 9:
        print("Invalid position!")
        continue

    if board[choice - 1] in ["X", "O"]:
        print("Position already occupied!")
        continue

    board[choice - 1] = "X"

    if check_winner(board, "X"):
        display(board)
        print("You Win!")
        break

    # Check draw
    if all(x in ["X", "O"] for x in board):
        display(board)
        print("Draw!")
        break

    # AI move
    print("AI Robot's turn...")
    ai_move(board)

    if check_winner(board, "O"):
        display(board)
        print("AI Robot Wins!")
        break
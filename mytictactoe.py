#Set up board
board = []
# TODO: Set up the board as a 3x3 grid of spaces here...
row = [' ', ' ', ' ']
for i in range (3):
    board.append(row)

# Print the board.
def print_board(x):
    # TODO: Replace the line below with your code...
    for i in range(3):
        print(x[i])

print_board(board)

# x goes first
turn = "x"

# Play tic tac toe
while not game_is_over(board):
    print_board(board)
    print("It's " + turn + "'s turn.")
    row = get_valid_index("Row: ")
    col = get_valid_index("Col: ")
    if board[row][column] == ' ':
        board[row][column] = turn
        if turn = 'x':
            turn = 'o'
        else:
            turn = 'x'
    else:
        print('This space is taken')


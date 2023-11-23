# Initialize the game board
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# Function to print the game board
def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))

# Function to check if the game has been won
def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0]:
            return True

    for col in range(len(board)):
        check_col = []
        for row in board:
            check_col.append(row[col])
        if check_col.count(check_col[0]) == len(check_col) and check_col[0]:
            return True

    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

# Function to check if the game has ended in a draw
def check_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

# Function to check if a move is valid
def valid_move(row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 0

# Function to handle player moves
def player_move(player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row col): ").split())
            if valid_move(row, col):
                board[row][col] = player
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter the row and column as numbers.")

# Main game
PLAYER_X = 'X'  
PLAYER_O = 'O'  

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board, player):
  
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_O): return 1
    if check_winner(board, PLAYER_X): return -1
    if is_board_full(board): return 0

    best = -float('inf') if is_maximizing else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_O if is_maximizing else PLAYER_X
                score = minimax(board, depth + 1, not is_maximizing)
                board[i][j] = ' '
                best = max(best, score) if is_maximizing else min(best, score)
    return best

def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_O
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def human_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] == ' ':
                return row, col
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2 for row and column.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        row, col = human_move(board)
        board[row][col] = PLAYER_X
        print_board(board)
        
        if check_winner(board, PLAYER_X):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        
        print("AI is making a move...")
        row, col = best_move(board)
        board[row][col] = PLAYER_O
        print_board(board)

        if check_winner(board, PLAYER_O):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
play_game()
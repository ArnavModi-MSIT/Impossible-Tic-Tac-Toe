def print_board(board):
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print("---|---|---")

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf'), use_alpha_beta=False):
    if check_win(board, 'O'):
        return 10 - depth
    if check_win(board, 'X'):
        return depth - 10
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta, use_alpha_beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    if use_alpha_beta:
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            return max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta, use_alpha_beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    if use_alpha_beta:
                        beta = min(beta, eval)
                        if beta <= alpha:
                            return min_eval
        return min_eval

def best_move(board, use_alpha_beta=False):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, use_alpha_beta=use_alpha_beta)
                board[i][j] = ' '
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'X'
    ai = 'O'
    current_player = human

    while True:
        print_board(board)
        if check_win(board, ai):
            print("AI wins!")
            break
        if check_win(board, human):
            print("Human wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        if current_player == human:
            print("Human's turn")
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if board[row][col] == ' ':
                    board[row][col] = human
                    current_player = ai
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 1 and 3.")
        else:
            print("AI's turn")
            row, col = best_move(board, use_alpha_beta=True)
            board[row][col] = ai
            current_player = human

if __name__ == "__main__":
    play_game()

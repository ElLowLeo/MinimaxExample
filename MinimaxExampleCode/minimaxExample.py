def evaluateBoard(board):

    winningCombinations = [ # All ways to win a tic tac toe game
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lines
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    # For example 
    # [0, 1, 2]
    # Means: 
    # X | X | X
    # ---------
    #   |   | 
    # ---------
    #   |   | 
    # Because:
    # 0 | 1 | 2
    # ---------
    # 3 | 4 | 5
    # ---------
    # 6 | 7 | 8

    for combo in winningCombinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            if board[combo[0]] == "X":
                return 10
            elif board[combo[0]] == "O":
                return -10

    if "" not in board:
        return 0  # Draw
    return None  # Game isn't over

def minimax(board, depth, isMaximizing):
    if depth == 0 or evaluateBoard(board) is not None:
        return evaluateBoard(board)

    if isMaximizing:
        maxEval = -float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                eval = minimax(board, depth - 1, False)
                maxEval = max(maxEval, eval)
                board[i] = ""
        return maxEval
    else:
        minEval = float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                eval = minimax(board, depth - 1, True)
                minEval = min(minEval, eval)
                board[i] = ""
        return minEval

def findBestMove(board):
    bestEval = -float('inf')
    bestMove = None
    for i in range(9):
        if board[i] == "":
            board[i] = "X"
            moveEval = minimax(board, 9, False)
            board[i] = ""
            if moveEval > bestEval:
                bestEval = moveEval
                bestMove = i
    return bestMove

def printBoard(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def main():
    initialBoard = ["X", "X", "O", "O", "O", "X", "X", "", ""]
    print("Initial board:")
    printBoard(initialBoard)

    bestMoveIndex = findBestMove(initialBoard)
    initialBoard[bestMoveIndex] = "\033[0;31mX\033[0m" # Red colored X scape sequence

    print("Board after the best move:")
    printBoard(initialBoard)

if __name__ == "__main__":
    main()

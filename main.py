import chess

def legal_moves(board):
    move_list = []
    for legal_move in board.legal_moves:
        legal_move = str(legal_move)
        move_list.append(legal_move)  # Print each legal move

    for move in move_list:
        print(str(move), end=", ")
    print("")




def main():
    board = chess.Board()
    print(board)

    while not board.is_game_over():
        print("Legal moves:")
        legal_moves(board)
        move = input("Your move: ")
        if chess.Move.from_uci(move) in board.legal_moves:
            try:
                board.push(chess.Move.from_uci(move))  # Add the move to the board.
            except:
                board.pop()
                print(f"{move} is not valid")
            print(board)
        else:
            print("Invalid move, try again!")

        if board.is_game_over():
            break
    
main()
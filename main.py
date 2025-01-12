import chess, random

class ChessGame:

    def __init__(self):
        board = chess.Board()

        name = input("Enter your name: ")
        while colour != "white" and colour != "black":
            colour = input("Enter your colour (white or black) or press enter to play a random colour: ")
            if colour.lower() == "white" or colour.lower() == "w":
                colour = "white"
            elif colour.lower() == "black" or colour.lower() == "b":
                colour = "black"
            elif colour == "":
                colour = random.choice(["white", "black"])
            else:
                print("Invalid colour. Please enter 'white' or 'black'.")

        elo = input("if you have an elo please enter it here: (if not press enter)")
        if elo == "":
            elo = 300

        return board, name, colour, elo

    def main(self):
        '''
            where the game starts
            loops through the game until the game is over
            makes move in uci format
            then calls the bot to make move
        '''
        board, name, colour, elo = self.__init__()
        print(board)
        while not board.is_game_over():
            print("Legal moves:")
            self.legal_moves(board)
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
    
    def legal_moves(self, board):
        '''
            prints each legal move for every turn

            prints the move in the UCI format: 'e2e4'
        '''
        move_list = []
        for legal_move in board.legal_moves:
            legal_move = str(legal_move)
            move_list.append(legal_move)  # Print each legal move

        for move in move_list:
            print(str(move), end=", ")
        print("")

    def change_elo(self, board, elo):
        '''
            changes elo depending on the outcome of the game

            elo += piecevalue_diff * 2 / (1 + 10 ** (rating_diff / 400))
        '''
        pass

    def piecevalue_diff(self, board):
        '''
            Calculates the worth of the position in terms of material value

            King = 0
            Queen = 9
            Rook = 5
            Bishop = 3
            Knight = 3
            Pawn = 1
        '''
        pass

    def bot_move(self, board, bot_move):
        pass

class Bot:
    '''
        this is where the neural network will be implemented

        elo += 105% of player_value
        colour = player_opposite if ! picked else: random.choice(white, black)
    '''
    def __init__(self, colour, elo, name):
        pass

    def move(self, board):
        pass

    



if __name__ == "__main__":
    game = ChessGame()
    game.main()
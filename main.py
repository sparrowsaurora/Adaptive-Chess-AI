import chess, random

class ChessGame:

    def __init__(self):
        # make board
        self.board = chess.Board()

        # Username
        # self.name = input("Enter your name: ")
        self.name = "temp"
        # Colour
        # self.colour = ""
        # while self.colour != "white" and self.colour != "black":
        #     self.colour = input("Enter your colour (white or black) or press enter to play a random colour: ")
        #     if self.colour.lower() == "white" or self.colour.lower() == "w":
        #         self.colour = "white"
        #         bot_colour = "black"
        #     elif self.colour.lower() == "black" or self.colour.lower() == "b":
        #         self.colour = "black"
        #         bot_colour = "white"
        #     elif self.colour == "":
        #         self.colour = random.choice(["white", "black"])
        #     else:
        #         print("Invalid colour. Please enter 'white' or 'black'. ")
        self.colour = "white"
        bot_colour = "black"
        # Elo
        # self.elo = input("if you have an elo please enter it here: (if not press enter)")
        # if self.elo == "":
        #     self.elo = 300
        
        self.elo = 300

        self.Bot = Bot(bot_colour, int(self.elo))

        return None

    def main(self):
        '''
            where the game starts
            loops through the game until the game is over
            makes move in uci format
            then calls the bot to make move
        '''
        print(self.board)
        while not self.board.is_game_over():
            print("Legal moves:")
            move_list = self.list_legal_moves()
            for move in move_list:
                print(str(move), end=", ")
            print("\n")
            move = input("Your move: ")
            if chess.Move.from_uci(move) in self.board.legal_moves:
                try:
                    self.board.push(chess.Move.from_uci(move)) # Add the move to the board.
                except:
                    self.board.pop()
                    print(f"{move} is not valid")
            else:
                print("Invalid move, try again!")
            bot_move_list = self.list_legal_moves()
            bot_move = self.Bot.move(bot_move_list)
            self.board.push(chess.Move.from_uci(bot_move))

            print(f"Bot played: {bot_move}")

            print(self.board)

            if self.board.is_game_over():
                print(chess.Board.outcome().winner())
                break
    
    def list_legal_moves(self):
        '''
            prints each legal move for every turn

            prints the moves in the UCI format: 'e2e4'
        '''
        move_list = []
        for legal_move in self.board.legal_moves:
            legal_move = str(legal_move)
            move_list.append(legal_move)  # Print each legal move

        return move_list

    def change_elo(self, board, elo):
        '''
            changes elo depending on the outcome of the game

            elo += piecevalue_diff * 1 / (1 + 10 ** (rating_diff / 400))
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
    def __init__(self, bot_colour, elo):
        self.colour = bot_colour
        self.bot_elo = round(float(elo) * 1.05)
        self.name = random.choice(["bot_1", "bot_2", "bot_3"])
        print(self.colour, self.bot_elo, self.name)
        return None

    def move(self, move_list):
        '''
            this is a temporary function
            Bot makes a random move from the list of legal moves.
            The chess library ensures the move is valid for the bot's color.
        '''
        return random.choice(move_list)

    



if __name__ == "__main__":
    game = ChessGame()
    game.main()
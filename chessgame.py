import chess
from bot import Bot
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
        
        self.elo = 1000

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

            # Prints list of legal moves
            print("Legal moves:")
            move_list = self.list_legal_moves()
            print(", ".join(move_list))

            # prompts for user's move + error handling
            move = input("Your move: ")
            if chess.Move.from_uci(move) in self.board.legal_moves:
                try:
                    self.board.push(chess.Move.from_uci(move)) # Add the move to the board.
                except:
                    self.board.pop()
                    print(f"{move} is not valid")
            else:
                print("Invalid move, try again!")
                continue

            # bot's move
            bot_move = self.Bot.move(self.board)
            self.board.push(chess.Move.from_uci(bot_move))
            print(f"Bot played: {bot_move}")
            
            #  prints updated board
            print(self.board)

            #checks for win condition
            if self.board.is_game_over():
                print("Game Over!")
                outcome = self.board.outcome()
                if outcome.winner is None:
                    print("It's a draw!")
                elif outcome.winner:
                    print("White wins!" if self.colour == "white" else "Black wins!")
                else:
                    print("Black wins!" if self.colour == "black" else "White wins!")
    
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
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
        
        self.elo = 3000

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

class Bot:
    '''
        This is where the neural network will be implemented.

        elo += 105% of player_value
        colour = player_opposite if ! picked else: random.choice(white, black)
    '''
    def __init__(self, bot_colour, elo):
        self.colour = bot_colour
        self.bot_elo = round(float(elo) * 1.05)
        self.name = random.choice(["bot_1", "bot_2", "bot_3"])
        print(self.colour, self.bot_elo, self.name)
        return None

    def evaluate_board(self, board):
        '''
            Evaluates the board and gives it a score based on the pieces on the board.
            + for white's favour, - for black's favour.
        '''
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0  # because the game ends if captured
        }
        score = 0
        for position in chess.SQUARES:
            piece = board.piece_at(position)
            if piece:
                value = piece_values[piece.piece_type]
                if piece.color:
                    score += value
                else:
                    score -= value
        return score

    def minimax_alpha_beta(self, board, depth, alpha, beta, is_maximizing):
        '''
            This is the smart part of the bot. It looks ahead to see the best moves.
            Alpha = the best value the maximizing player can get.
            Beta = the best value the minimizing player can get.
        '''
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        if is_maximizing:
            max_eval = float("-inf")
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax_alpha_beta(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:  # Cut off the search if it's no longer useful
                    break
            return max_eval
        else:
            min_eval = float("inf")
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax_alpha_beta(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:  # Cut off the search if it's no longer useful
                    break
            return min_eval

    def move(self, board):
        '''
            The Bot calculates the best move using the minimax algorithm with alpha-beta pruning.
        '''
        best_move = None
        best_value = float("-inf") if self.colour == "white" else float("inf")

        for move in board.legal_moves:
            board.push(move)

             # Calculate alpha-beta pruning depth based on player ELO
            elo_depth_map = {
                0: 1,  # Beginner
                1000: 2,  # Casual
                1500: 3,  # Intermediate
                2000: 4,  # Advanced
                2500: 5,  # Expert
                3000: 6  # Master
            }
            depth = 2  # Default depth
            for elo, depth_eqiv in elo_depth_map.items():
                if self.bot_elo <= elo:
                    depth = depth_eqiv
                    break

                # Evaluate move using minimax
            move_value = self.minimax_alpha_beta(board, depth=depth, alpha=float("-inf"), beta=float("inf"), is_maximizing=(self.colour == "black"))
            board.pop()

            # Find best move
            if (self.colour == "white" and move_value > best_value) or (self.colour == "black" and move_value < best_value):
                best_value = move_value
                best_move = move

        return best_move.uci()


if __name__ == "__main__":
    game = ChessGame()
    game.main()
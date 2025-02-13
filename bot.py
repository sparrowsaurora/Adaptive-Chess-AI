import chess, random
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
        # Base case: If the game is over or the maximum depth is reached, return the evaluation score.
        if depth == 0 or board.is_game_over():  
            return self.evaluate_board(board)  # Evaluate the current state of the game.

        if is_maximizing:
            max_eval = float("-inf")  # Initialize the best evaluation score for the maximizing player.
            for move in board.legal_moves:
                board.push(move)  # Make the move on the board.
                eval = self.minimax_alpha_beta(board, depth - 1, alpha, beta, False)  # Recursively call for the minimizing player.
                board.pop()  # Undo the move on the board.
                max_eval = max(max_eval, eval)  # Update the best evaluation score.
                alpha = max(alpha, eval)  # Update alpha.
                if beta <= alpha:  # Prune the search tree if beta is less than or equal to alpha.
                    break
            return max_eval  # Return the best evaluation score found.

        else:
            min_eval = float("inf")  # Initialize the best evaluation score for the minimizing player.
            for move in board.legal_moves:
                board.push(move)  # Make the move on the board.
                eval = self.minimax_alpha_beta(board, depth - 1, alpha, beta, True)  # Recursively call for the maximizing player.
                board.pop()  # Undo the move on the board.
                min_eval = min(min_eval, eval)  # Update the best evaluation score.
                beta = min(beta, eval)  # Update beta.
                if beta <= alpha:  # Prune the search tree if beta is less than or equal to alpha.
                    break
            return min_eval  # Return the best evaluation score found.

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
                3000: 6,  # Master
                3500: 7  # Grandmaster
            }
            depth = 2  # Default depth
            for elo, d in elo_depth_map.items():
                if self.bot_elo <= elo:
                    depth = d
                    break
            else:
                depth = 7  # Use the maximum depth for ELO values above 3000
                print(f"Warning: ELO {self.bot_elo} is higher than the maximum value in the ELO depth map")

            # Evaluate move using minimax
            move_value = self.minimax_alpha_beta(
                board, 
                depth=depth, 
                alpha=float("-inf"), 
                beta=float("inf"), 
                is_maximizing=(self.colour == "black")
            )
            print(f"Move value: {move_value}")
            board.pop()

            # Find best move
            if (self.colour == "white" and move_value > best_value) or (self.colour == "black" and move_value < best_value):
                best_value = move_value
                best_move = move

        return best_move.uci()
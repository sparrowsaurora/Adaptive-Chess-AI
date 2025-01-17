# Adaptive Chess Bot

An adaptive chess bot written in Python that analyses the player's skill level and adjusts its gameplay to match or slightly surpass it.
currently we are using an minimax algorithm with Alpha Beta Pruning to make the best possible move.  
_Currently any elo above 1800 will take more than 10 seconds to generate a response move_

## Features

- Dynamic Difficulty Adjustment: The bot assesses the player's skill level during gameplay and adapts accordingly.

- Chess Engine: Implements all standard chess rules, including special moves (castling, en passant, pawn promotion) and game-end conditions (checkmate, stalemate).

- Evaluation Function: Calculates the best move using a heuristic-based board evaluation.

- Minimax Algorithm with Alpha-Beta Pruning: Ensures efficient decision-making.

- Skill Tracking: Tracks player performance metrics like blunders and move quality.

- User Interface:

    - Command-line interface (CLI) for initial interaction.

    - Graphical User Interface (GUI) using pygame or tkinter for a more polished experience.

---

## Installation

1. Clone the repository:

    ``` bash
    git clone https://github.com/yourusername/adaptive-chess-bot.git
    cd adaptive-chess-bot
    ```

2. Set up a Python virtual environment (optional but recommended):

    ``` bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4. Run the bot:

    ``` bash
    python main.py
    ```

## How It Will Work

1. Chessboard Logic:

    - The chessboard is represented as an 8x8 grid.

    - Move generation and validation ensure compliance with chess rules.

2. Bot Logic:

    - The bot uses the Minimax algorithm with Alpha-Beta Pruning for efficient move calculation.

    - A heuristic evaluation function calculates the optimal move.

3. Skill Adaptation:

    - Tracks metrics like move time and blunders to estimate player skill.

    - Adjusts search depth and move quality based on the player's performance.

4. User Interface:

    - The CLI allows users to input moves in standard chess notation (e.g., e2e4).

    - The GUI provides a visual chessboard for an interactive experience.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request. For major changes, please open a discussion first to propose your ideas.

## To Do

- improve algorithm
- add calculation, adjustion and saving method for elo
- add gui
- adapt algorithm strength depending on elo

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact

LinkedIn: Your Profile

GitHub: [Sparrowsaurora](https://github.com/sparrowsaurora)

Email: [sparrows.au@gmail.com](mailto:sparrows.au@gmail.com)

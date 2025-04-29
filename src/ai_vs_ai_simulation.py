import pandas as pd
import matplotlib.pyplot as plt
from tictactoe import TicTacToe
import random

def minimax(board, player, depth=3):
    max_player = "X"
    other_player = "O" if player == "X" else "X"

    if depth == 0 or board.current_winner == other_player:
        if board.current_winner == max_player:
            return {'position': None, 'score': 1}
        elif board.current_winner == other_player:
            return {'position': None, 'score': -1}
        else:
            return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -float('inf')}
    else:
        best = {'position': None, 'score': float('inf')}

    for possible_move in board.available_moves():
        board.make_move(possible_move, player)
        sim_score = minimax(board, other_player, depth-1)

        board.board[possible_move] = " "
        board.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score

    return best

def play_game():
    game = TicTacToe()
    letter = random.choice(["X", "O"])

    while game.empty_squares():
        if random.random() < 0.1:
            move = random.choice(game.available_moves())
        else:
            random_depth = random.randint(1, 4)
            move = minimax(game, letter, depth=random_depth)['position']

        if move is None:
            break
        game.make_move(move, letter)

        if game.current_winner:
            return letter
        letter = "O" if letter == "X" else "X"

    return "Draw"

def simulate_games(n_games):
    results = {"X wins": 0, "O wins": 0, "Draw": 0}
    for _ in range(n_games):
        result = play_game()
        results_key = {
            "X": "X wins",
            "O": "O wins",
            "Draw": "Draw"
        }[result]
        results[results_key] += 1
    return results

if __name__ == "__main__":
    n_sets = 5
    n_games_per_set = 50

    all_results = []

    for i in range(n_sets):
        set_result = simulate_games(n_games_per_set)
        print(f"Set {i+1}: {set_result}")
        all_results.append(set_result)

    # pandas로 변환
    df = pd.DataFrame(all_results, index=[f"Set {i+1}" for i in range(n_sets)])
    print("\n=== Summary ===")
    print(df)

    # Bar Chart 그리기
    df.plot(kind="bar", figsize=(10,6))
    plt.title("Tic-Tac-Toe AI Simulation Results (5 Sets)")
    plt.xlabel("Set")
    plt.ylabel("Number of Wins / Draws")
    plt.xticks(rotation=0)
    plt.legend(title="Result")
    plt.tight_layout()
    plt.show()

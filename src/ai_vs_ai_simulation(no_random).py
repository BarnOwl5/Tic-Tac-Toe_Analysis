from tictactoe import TicTacToe
import random

def minimax(board, player):
    max_player = "X"  # 공격자
    other_player = "O" if player == "X" else "X"

    # 종료 조건: 승자 있거나 무승부
    if board.current_winner == other_player:
        return {'position': None, 'score': 1 * (board.num_empty_squares() + 1) if other_player == max_player else -1 * (board.num_empty_squares() + 1)}
    elif not board.empty_squares():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -float('inf')}
    else:
        best = {'position': None, 'score': float('inf')}

    for possible_move in board.available_moves():
        board.make_move(possible_move, player)
        sim_score = minimax(board, other_player)  # 재귀 호출

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
    letter = "X"  # X부터 시작

    while game.empty_squares():
        if letter == "O":
            move = minimax(game, "O")['position']
        else:
            move = minimax(game, "X")['position']

        if move is None:  # 무승부
            break
        game.make_move(move, letter)

        if game.current_winner:
            return letter  # 승자 반환
        letter = "O" if letter == "X" else "X"

    return "Draw"

def simulate_games(n_games):
    results = {"X wins": 0, "O wins": 0, "Draw": 0}
    for _ in range(n_games):
        result = play_game()
        if result == "X":
            results["X wins"] += 1
        elif result == "O":
            results["O wins"] += 1
        else:
            results["Draw"] += 1
    return results

if __name__ == "__main__":
    n_games = 1000
    results = simulate_games(n_games)
    print(f"Simulated {n_games} games:")
    print(results)

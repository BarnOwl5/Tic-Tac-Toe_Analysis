# tictactoe.py
import sys, os
sys.path.append(os.path.dirname(__file__))

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 칸
        self.current_winner = None

    def make_move(self, square, letter):
        # 해당 칸이 비어있으면 말 놓기
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # 승리 체크
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def empty_squares(self):
        return " " in self.board

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def num_empty_squares(self):
        return self.board.count(" ")

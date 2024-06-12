import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from game_state import GameState
from application_menu import ApplicationMenu
from player_layout import PlayerLayout

class SuperTicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Супер Крестики-Нолики")
        self.setGeometry(250, 50, 1400, 900)
        self.setStyleSheet("background-color: #2B2B2B; color: white;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()
        self.grid_layout.setContentsMargins(0, 50, 0, 0)
        self.grid_layout.setSpacing(0)
        self.main_layout = QGridLayout()
        self.central_widget.setLayout(self.main_layout)

        self.state = GameState()

        self.current_player_label = QLabel(f"Текущий игрок: {self.state.current_player}")
        self.player_layout_x = PlayerLayout("Игрок X", "x", self.state)
        self.player_layout_o = PlayerLayout("Игрок O", "o", self.state)

        self.appMenu = ApplicationMenu(self, self.state)

        self.initUI()

    def initUI(self):
        self.current_player_label.setFont(QFont("Georgia", 16))
        self.main_layout.addWidget(self.current_player_label, 1, 1, Qt.AlignCenter)
        self.main_layout.addLayout(self.player_layout_x, 0, 0, Qt.AlignTop)
        self.main_layout.addLayout(self.player_layout_o, 0, 2, Qt.AlignTop)

        self.main_layout.addLayout(self.grid_layout, 0, 1)
        self.grid_layout_widget = QWidget()
        self.grid_layout_widget.setLayout(self.grid_layout)
        self.grid_layout_widget.setStyleSheet("background-color: 2B2B2B;")
        self.main_layout.addWidget(self.grid_layout_widget, 0, 1)

        for row in range(self.state.board_size):
            for col in range(self.state.board_size):
                sub_board = QWidget()
                sub_board_layout = QGridLayout()
                sub_board.setLayout(sub_board_layout)
                sub_board.setStyleSheet("background-color: black;")
                self.state.board[row][col] = [[None for _ in range(self.state.sub_board_size)] for _ in
                                              range(self.state.sub_board_size)]

                for sub_row in range(self.state.sub_board_size):
                    for sub_col in range(self.state.sub_board_size):
                        button = QPushButton("")
                        button.setFixedSize(80, 80)
                        button.setStyleSheet(
                            f"font-size: 60px; border: 1px solid black; background-color: {self.state.colour_main}; color: white;")
                        button.clicked.connect(
                            lambda checked, r=row, c=col, sr=sub_row, sc=sub_col: self.make_move(r, c, sr, sc))
                        sub_board_layout.addWidget(button, sub_row, sub_col)
                        self.state.board[row][col][sub_row][sub_col] = button

                self.grid_layout.addWidget(sub_board, row, col)

        self.highlight_available_moves()

        self.appMenu.initUI()

    def make_move(self, row, col, sub_row, sub_col):
        if self.state.game_over or self.state.board[row][col][sub_row][sub_col].text() != "" or (
                self.state.sub_board_status[row][col] is not None):
            return
        if self.state.next_board and self.state.next_board != (row, col):
            return

        current_player_name = self.state.player_o_name if self.state.current_player == "⛌" else self.state.player_x_name
        current_player_name1 = self.state.player_x_name if self.state.current_player == "⛌" else self.state.player_o_name

        self.state.board[row][col][sub_row][sub_col].setText(self.state.current_player)
        if self.state.current_player == "⛌":
            self.state.board[row][col][sub_row][sub_col].setStyleSheet(
                f"font-size: 60px; color: {self.state.colour_x}; background-color: {self.state.colour_main};")
        else:
            self.state.board[row][col][sub_row][sub_col].setStyleSheet(
                f"font-size: 60px; color: {self.state.colour_o}; background-color: {self.state.colour_main};")

        if self.state.check_sub_board_winner(row, col):
            self.state.sub_board_status[row][col] = self.state.current_player
            self.update_sub_board(row, col, self.state.current_player)
            if self.state.check_winner():
                self.state.game_over = True
                QMessageBox.information(self, "Конец игры", f" {current_player_name1} победил(а)!")
                self.state.reset_board()
                return
        elif self.state.check_draw(row, col):
            self.state.sub_board_status[row][col] = "Draw"
            self.state.game_over = True
            QMessageBox.information(self, "Конец игры", "Ничья!")
            self.state.reset_board()
            return
        self.state.current_player = "㋡" if self.state.current_player == "⛌" else "⛌"
        self.current_player_label.setText(f"Текущий игрок: {current_player_name}")
        self.state.next_board = (sub_row, sub_col) if self.state.sub_board_status[sub_row][sub_col] is None else None
        self.highlight_available_moves()

    def update_sub_board(self, row, col, winner):
        overlay = QLabel(self.grid_layout.itemAtPosition(row, col).widget())

        overlay.setText(winner)
        overlay.setAlignment(Qt.AlignCenter)
        if winner == "⛌":
            overlay.setStyleSheet(
                f"font-size: 230px; color: {self.state.colour_x}; background-color: {self.state.colour_main};")
        else:
            overlay.setStyleSheet(
                f"font-size: 230px; color: {self.state.colour_o}; background-color: {self.state.colour_main};")
        overlay.setGeometry(10, 10, 255, 255)
        overlay.setAlignment(Qt.AlignCenter)
        overlay.setAttribute(Qt.WA_TransparentForMouseEvents)
        overlay.show()

    def highlight_available_moves(self):
        for row in range(self.state.board_size):
            for col in range(self.state.board_size):
                for sub_row in range(self.state.sub_board_size):
                    for sub_col in range(self.state.sub_board_size):
                        button = self.state.board[row][col][sub_row][sub_col]
                        if button.text() == "" and (
                                self.state.next_board is None or self.state.next_board == (row, col)):
                            button.setStyleSheet(
                                f"font-size: 24px; background-color: {self.state.highlight_colour}; color: white;")
                        elif button.text() == "":
                            button.setStyleSheet(
                                f"font-size: 24px; background-color: {self.state.colour_main}; color: white;")
                        elif button.text() == "⛌":
                            button.setStyleSheet(
                                f"font-size: 60px; color: {self.state.colour_x}; background-color: {self.state.colour_main};")
                        elif button.text() == "㋡":
                            button.setStyleSheet(
                                f"font-size: 60px; color: {self.state.colour_o}; background-color: {self.state.colour_main};")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = SuperTicTacToe()
    game.show()
    sys.exit(app.exec_())

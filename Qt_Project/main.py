import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QAction, QColorDialog, QFileDialog, QMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

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

        self.board_size = 3
        self.sub_board_size = 3
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.sub_board_status = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = "⛌"
        self.game_over = False
        self.next_board = None

        self.playerX_name = QLineEdit("Игрок X")
        self.playerX_name.setFont(QFont("Georgia", 14))
        self.playerO_name = QLineEdit("Игрок O")
        self.playerO_name.setFont(QFont("Georgia", 14))
        self.playerX_photo = QLabel()
        self.playerO_photo = QLabel()
        self.playerX_photo_path = "default_photo.jpg"
        self.playerO_photo_path = "default_photo.jpg"
        self.photo_size = 150

        self.colour_x = "black"
        self.colour_o = "black"
        self.colour_main = "white"
        self.highlight_colour = "#E768AD"

        self.initUI()

    def initUI(self):
        playerX_layout = QVBoxLayout()
        playerX_label = QLabel("Игрок X:")
        playerX_label.setFont(QFont("Georgia", 16))
        playerX_layout.addWidget(playerX_label)
        playerX_layout.addWidget(self.playerX_name)
        self.playerX_photo.setPixmap(QPixmap(self.playerX_photo_path).scaled(self.photo_size, self.photo_size, Qt.KeepAspectRatio))
        playerX_layout.addWidget(self.playerX_photo, 0, Qt.AlignCenter)
        playerX_photo_button = QPushButton("Добавить фото")
        playerX_photo_button.setStyleSheet("background-color: white; color: 2B2B2B;")
        playerX_photo_button.setFont(QFont("Original", 10))
        playerX_photo_button.clicked.connect(lambda: self.upload_photo(1))
        playerX_layout.addWidget(playerX_photo_button)

        playerO_layout = QVBoxLayout()
        playerO_label = QLabel("Игрок O:")
        playerO_label.setFont(QFont("Georgia", 16))
        playerO_layout.addWidget(playerO_label)
        playerO_layout.addWidget(self.playerO_name)
        self.playerO_photo.setPixmap(QPixmap(self.playerO_photo_path).scaled(self.photo_size, self.photo_size, Qt.KeepAspectRatio))
        playerO_layout.addWidget(self.playerO_photo, 0, Qt.AlignCenter)
        playerO_photo_button = QPushButton("Добавить фото")
        playerO_photo_button.setStyleSheet("background-color: white; color: 2B2B2B;")
        playerO_photo_button.setFont(QFont("Original", 10))
        playerO_photo_button.clicked.connect(lambda: self.upload_photo(2))
        playerO_layout.addWidget(playerO_photo_button)

        self.current_player_label = QLabel(f"Текущий игрок: {self.current_player}")
        self.current_player_label.setFont(QFont("Georgia", 16))
        self.main_layout.addWidget(self.current_player_label, 1, 1, Qt.AlignCenter)

        self.main_layout.addLayout(playerX_layout, 0, 0, Qt.AlignTop)
        self.main_layout.addLayout(playerO_layout, 0, 2, Qt.AlignTop)

        self.main_layout.addLayout(self.grid_layout, 0, 1)
        self.grid_layout_widget = QWidget()
        self.grid_layout_widget.setLayout(self.grid_layout)
        self.grid_layout_widget.setStyleSheet("background-color: 2B2B2B;")
        self.main_layout.addWidget(self.grid_layout_widget, 0, 1)

        for row in range(self.board_size):
            for col in range(self.board_size):
                sub_board = QWidget()
                sub_board_layout = QGridLayout()
                sub_board.setLayout(sub_board_layout)
                sub_board.setStyleSheet("background-color: black;")
                self.board[row][col] = [[None for _ in range(self.sub_board_size)] for _ in range(self.sub_board_size)]

                for sub_row in range(self.sub_board_size):
                    for sub_col in range(self.sub_board_size):
                        button = QPushButton("")
                        button.setFixedSize(80, 80)
                        button.setStyleSheet(f"font-size: 60px; border: 1px solid black; background-color: {self.colour_main}; color: white;")
                        button.clicked.connect(
                            lambda checked, r=row, c=col, sr=sub_row, sc=sub_col: self.make_move(r, c, sr, sc))
                        sub_board_layout.addWidget(button, sub_row, sub_col)
                        self.board[row][col][sub_row][sub_col] = button

                self.grid_layout.addWidget(sub_board, row, col)

        self.highlight_available_moves()

        menubar = self.menuBar()
        menubar.setStyleSheet("background-color: #2B2B2B; color: white;")
        state_menu = menubar.addMenu("State")
        edit_menu = menubar.addMenu("Edit")

        load_action = QAction("Load", self)
        save_action = QAction("Save", self)
        reset_action = QAction("Reset", self)
        state_menu.addAction(load_action)
        state_menu.addAction(save_action)
        state_menu.addAction(reset_action)
        load_action.triggered.connect(self.load_game)
        save_action.triggered.connect(self.save_game)
        reset_action.triggered.connect(self.reset_board)

        colour_menu = QMenu("Изменить цвета", self)
        change_colour_x_action = QAction("Цвет X", self)
        change_colour_o_action = QAction("Цвет O", self)
        change_colour_main_action = QAction("Главный цвет", self)
        change_highlight_colour_action = QAction("Дополнительный цвет", self)

        colour_menu.addAction(change_colour_x_action)
        colour_menu.addAction(change_colour_o_action)
        colour_menu.addAction(change_colour_main_action)
        colour_menu.addAction(change_highlight_colour_action)

        edit_menu.addMenu(colour_menu)

        change_colour_x_action.triggered.connect(lambda: self.change_colour("X"))
        change_colour_o_action.triggered.connect(lambda: self.change_colour("O"))
        change_colour_main_action.triggered.connect(lambda: self.change_colour("main"))
        change_highlight_colour_action.triggered.connect(lambda: self.change_colour("highlight"))

    def upload_photo(self, player):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Photo", "", "Image Files (*.png *.jpg *.bmp)",
                                                   options=options)
        if file_name:
            pixmap = QPixmap(file_name).scaled(300, 300, Qt.KeepAspectRatio)
            if player == 1:
                self.playerX_photo_path = file_name
                self.playerX_photo.setPixmap(pixmap)
            else:
                self.playerO_photo_path = file_name
                self.playerO_photo.setPixmap(pixmap)

    def save_game(self):
        game_state = {
            "board": [[[(button.text(), button.isEnabled()) for button in row] for row in col] for col in self.board],
            "sub_board_status": self.sub_board_status,
            "current_player": self.current_player,
            "game_over": self.game_over,
            "next_board": self.next_board,
            "colour_x": self.colour_x,
            "colour_o": self.colour_o,
            "colour_main": self.colour_main,
            "highlight_colour": self.highlight_colour
        }
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Game", "", "Game Files (*.game)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(str(game_state))

    def load_game(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load Game", "", "Game Files (*.game)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                game_state = eval(file.read())
                self.sub_board_status = game_state["sub_board_status"]
                self.current_player = game_state["current_player"]
                self.game_over = game_state["game_over"]
                self.next_board = game_state["next_board"]
                self.colour_x = game_state["colour_x"]
                self.colour_o = game_state["colour_o"]
                self.colour_main = game_state["colour_main"]
                self.highlight_colour = game_state["highlight_colour"]
                for row in range(self.board_size):
                    for col in range(self.board_size):
                        for sub_row in range(self.sub_board_size):
                            for sub_col in range(self.sub_board_size):
                                text, enabled = game_state["board"][row][col][sub_row][sub_col]
                                button = self.board[row][col][sub_row][sub_col]
                                button.setText(text)
                                button.setEnabled(enabled)
                                if text == "⛌":
                                    button.setStyleSheet(f"font-size: 60px; color: {self.colour_x}; background-color: {self.colour_main};")
                                elif text == "㋡":
                                    button.setStyleSheet(f"font-size: 60px; color: {self.colour_o}; background-color: {self.colour_main};")
                                else:
                                    button.setStyleSheet(f"font-size: 60px; background-color: {self.colour_main};")
                self.highlight_available_moves()

    def make_move(self, row, col, sub_row, sub_col):
        if self.game_over or self.board[row][col][sub_row][sub_col].text() != "" or (
                self.sub_board_status[row][col] is not None):
            return
        if self.next_board and self.next_board != (row, col):
            return

        current_player_name = self.playerO_name.text() if self.current_player == "⛌" else self.playerX_name.text()
        current_player_name1 = self.playerX_name.text() if self.current_player == "⛌" else self.playerO_name.text()

        self.board[row][col][sub_row][sub_col].setText(self.current_player)
        if self.current_player == "⛌":
            self.board[row][col][sub_row][sub_col].setStyleSheet(f"font-size: 60px; color: {self.colour_x}; background-color: {self.colour_main};")
        else:
            self.board[row][col][sub_row][sub_col].setStyleSheet(f"font-size: 60px; color: {self.colour_o}; background-color: {self.colour_main};")

        if self.check_sub_board_winner(row, col):
            self.sub_board_status[row][col] = self.current_player
            self.update_sub_board(row, col, self.current_player)
            if self.check_winner():
                self.game_over = True
                QMessageBox.information(self, "Конец игры", f" {current_player_name1} победил(а)!")
                self.reset_board()
                return
        elif self.check_draw(row, col):
            self.sub_board_status[row][col] = "Draw"
            self.game_over = True
            QMessageBox.information(self, "Конец игры", "Ничья!")
            self.reset_board()
            return
        self.current_player = "㋡" if self.current_player == "⛌" else "⛌"
        self.current_player_label.setText(f"Текущий игрок: {current_player_name}")
        self.next_board = (sub_row, sub_col) if self.sub_board_status[sub_row][sub_col] is None else None
        self.highlight_available_moves()

    def check_sub_board_winner(self, row, col):
        sub_board = self.board[row][col]
        for i in range(self.sub_board_size):
            if sub_board[i][0].text() == sub_board[i][1].text() == sub_board[i][2].text() != "":
                return True
            if sub_board[0][i].text() == sub_board[1][i].text() == sub_board[2][i].text() != "":
                return True
        if sub_board[0][0].text() == sub_board[1][1].text() == sub_board[2][2].text() != "":
            return True
        if sub_board[0][2].text() == sub_board[1][1].text() == sub_board[2][0].text() != "":
            return True
        return False

    def update_sub_board(self, row, col, winner):
        overlay = QLabel(self.grid_layout.itemAtPosition(row, col).widget())
        overlay.setText(winner)
        overlay.setAlignment(Qt.AlignCenter)
        if winner == "⛌":
            overlay.setStyleSheet(f"font-size: 230px; color: {self.colour_x}; background-color: {self.colour_main};")
        else:
            overlay.setStyleSheet(f"font-size: 230px; color: {self.colour_o}; background-color: {self.colour_main};")
        overlay.setGeometry(10, 10, 255, 255)
        overlay.setAttribute(Qt.WA_TransparentForMouseEvents)
        overlay.show()

    def check_draw(self, row, col):
        sub_board = self.board[row][col]
        for sub_row in range(self.sub_board_size):
            for sub_col in range(self.sub_board_size):
                if sub_board[sub_row][sub_col].text() == "":
                    return False
        return True
    def check_winner(self):
        for i in range(self.board_size):
            if self.sub_board_status[i][0] == self.sub_board_status[i][1] == self.sub_board_status[i][2] is not None:
                return True
            if self.sub_board_status[0][i] == self.sub_board_status[1][i] == self.sub_board_status[2][i] is not None:
                return True
        if self.sub_board_status[0][0] == self.sub_board_status[1][1] == self.sub_board_status[2][2] is not None:
            return True
        if self.sub_board_status[0][2] == self.sub_board_status[1][1] == self.sub_board_status[2][0] is not None:
            return True
        return False

    def reset_board(self):
        self.current_player = "⛌"
        self.game_over = False
        self.next_board = None
        self.current_player_label.setText(f"Текущий игрок: {self.current_player}")

        for row in range(self.board_size):
            for col in range(self.board_size):
                for sub_row in range(self.sub_board_size):
                    for sub_col in range(self.sub_board_size):
                        button = self.board[row][col][sub_row][sub_col]
                        button.setText("")
                        button.setEnabled(True)
                        button.setVisible(True)
                        button.setStyleSheet(f"font-size: 24px; background-color: {self.colour_main};")

                sub_board_widget = self.grid_layout.itemAtPosition(row, col).widget()
                for child in sub_board_widget.children():
                    if isinstance(child, QLabel):
                        child.deleteLater()
                self.sub_board_status[row][col] = None
        self.highlight_available_moves()

    def highlight_available_moves(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                for sub_row in range(self.sub_board_size):
                    for sub_col in range(self.sub_board_size):
                        button = self.board[row][col][sub_row][sub_col]
                        if button.text() == "" and (
                                self.next_board is None or self.next_board == (row, col)):
                            button.setStyleSheet(f"font-size: 24px; background-color: {self.highlight_colour}; color: white;")
                        elif button.text() == "":
                            button.setStyleSheet(f"font-size: 24px; background-color: {self.colour_main}; color: white;")
                        elif button.text() == "⛌":
                            button.setStyleSheet(f"font-size: 60px; color: {self.colour_x}; background-color: {self.colour_main};")
                        elif button.text() == "㋡":
                            button.setStyleSheet(f"font-size: 60px; color: {self.colour_o}; background-color: {self.colour_main};")

    def change_colour(self, piece):
        colour = QColorDialog.getColor()
        if colour.isValid():
            if piece == "X":
                self.colour_x = colour.name()
            elif piece == "O":
                self.colour_o = colour.name()
            elif piece == "main":
                self.colour_main = colour.name()
            elif piece == "highlight":
                self.highlight_colour = colour.name()
            self.highlight_available_moves()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = SuperTicTacToe()
    game.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QMenu, QAction, QLabel, QColorDialog
class ApplicationMenu(QMenu):
    def __init__(self, main_window, state):
        super().__init__()
        self.main_window = main_window
        self.state = state

    def initUI(self):
        menubar = self.main_window.menuBar()
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

    def save_game(self):
        self.state.save_game(self)

    def load_game(self):
        self.state.load_game(self)
        self.main_window.highlight_available_moves()
        self.main_window.player_layout_x.player_name.setText(self.state.player_x_name)
        self.main_window.player_layout_o.player_name.setText(self.state.player_o_name)
        current_name = self.state.player_x_name if self.state.current_player == "x" else self.state.player_o_name
        self.main_window.current_player_label.setText(f"Текущий игрок: {current_name}")

    def reset_board(self):
        self.state.reset_board()

        for row in range(self.state.board_size):
            for col in range(self.state.board_size):
                sub_board_widget = self.main_window.grid_layout.itemAtPosition(row, col).widget()
                for child in sub_board_widget.children():
                    if isinstance(child, QLabel):
                        child.deleteLater()

        self.main_window.current_player_label.setText(f"Текущий игрок: {self.state.current_player}")
        self.main_window.highlight_available_moves()

    def change_colour(self, piece):
        colour = QColorDialog.getColor()
        if colour.isValid():
            if piece == "X":
                self.state.colour_x = colour.name()
            elif piece == "O":
                self.state.colour_o = colour.name()
            elif piece == "main":
                self.state.colour_main = colour.name()
            elif piece == "highlight":
                self.state.highlight_colour = colour.name()
            self.main_window.highlight_available_moves()
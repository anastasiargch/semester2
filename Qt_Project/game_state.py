from PyQt5.QtWidgets import QFileDialog

class GameState:
    def __init__(self):
        self.board_size = 3
        self.sub_board_size = 3
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.sub_board_status = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = "⛌"
        self.game_over = False
        self.next_board = None

        self.colour_x = "black"
        self.colour_o = "black"
        self.colour_main = "white"
        self.highlight_colour = "#E768AD"

        self.player_x_name = "Игрок X"
        self.player_o_name = "Игрок O"

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

    def check_draw(self, row, col):
        sub_board = self.board[row][col]
        for sub_row in range(self.sub_board_size):
            for sub_col in range(self.sub_board_size):
                if sub_board[sub_row][sub_col].text() == "":
                    return False
        return True

    def save_game(self, menu):
        game_state = {
            "board": [[[[(button.text(), button.isEnabled()) for button in row] for row in col] for col in block] for
                      block in self.board],
            "sub_board_status": self.sub_board_status,
            "current_player": self.current_player,
            "game_over": self.game_over,
            "next_board": self.next_board,
            "colour_x": self.colour_x,
            "colour_o": self.colour_o,
            "colour_main": self.colour_main,
            "highlight_colour": self.highlight_colour,
            "player_x_name": self.player_x_name,
            "player_o_name": self.player_o_name,
        }
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(menu, "Save Game", "", "Game Files (*.game)",
                                                   options=options)

    def reset_board(self):
        self.current_player = "⛌"
        self.game_over = False
        self.next_board = None

        for row in range(self.board_size):
            for col in range(self.board_size):
                for sub_row in range(self.sub_board_size):
                    for sub_col in range(self.sub_board_size):
                        button = self.board[row][col][sub_row][sub_col]
                        button.setText("")
                        button.setEnabled(True)
                        button.setVisible(True)
                        button.setStyleSheet(
                            f"font-size: 24px; background-color: {self.colour_main};")
                self.sub_board_status[row][col] = None
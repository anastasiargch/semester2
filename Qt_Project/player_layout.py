from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QPushButton, QFileDialog


class PlayerLayout(QVBoxLayout):
    def __init__(self, player_title, player_id, state):
        super().__init__()
        self.player_title = player_title
        self.player_id = player_id
        self.state = state
        self.init_layout()

    def init_layout(self):
        self.player_name = QLineEdit(self.player_title)
        self.player_name.textEdited.connect(lambda text: self.change_name(text))

        self.player_name.setFont(QFont("Georgia", 14))
        self.player_photo = QLabel()
        self.photo_size = 300
        self.player_photo.setFixedWidth(300)
        self.player_photo_path = "default_photo.jpg"

        self.player_label = QLabel(f"{self.player_title}:")
        self.player_label.setFont(QFont("Georgia", 16))
        self.addWidget(self.player_label)
        self.addWidget(self.player_name)
        self.player_photo.setPixmap(
            QPixmap(self.player_photo_path).scaled(self.photo_size, self.photo_size, Qt.KeepAspectRatio))
        self.addWidget(self.player_photo, 0, Qt.AlignCenter)
        player_photo_button = QPushButton("Добавить фото")
        player_photo_button.setFixedWidth(self.photo_size)
        player_photo_button.setStyleSheet("background-color: white; color: 2B2B2B;")
        player_photo_button.setFont(QFont("Original", 10))
        player_photo_button.clicked.connect(lambda: self.upload_photo())
        self.addWidget(player_photo_button)

        if self.player_id == "x":
            self.player_name.setText(self.state.player_x_name)
        if self.player_id == "o":
            self.player_name.setText(self.state.player_o_name)

    def change_name(self, text):
        if self.player_id == "x":
            self.state.player_x_name = text
        if self.player_id == "o":
            self.state.player_o_name = text

    def upload_photo(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self.player_photo, "Select Photo", "",
                                                   "Image Files (*.png *.jpg *.bmp)",
                                                   options=options)
        if file_name:
            pixmap = QPixmap(file_name).scaled(self.photo_size, self.photo_size, Qt.KeepAspectRatio)
            self.player_photo_path = file_name
            self.player_photo.setPixmap(pixmap)

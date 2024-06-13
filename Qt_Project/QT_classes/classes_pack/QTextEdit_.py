from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget, QPushButton, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit Example")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit()
        self.text_edit.setPlainText("Hello, QTextEdit!")

        # Добавление кнопок для управления текстом
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)

        self.append_button = QPushButton("Append")
        self.append_button.clicked.connect(self.append_text)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.clear_button)
        self.button_layout.addWidget(self.append_button)

        self.layout.addLayout(self.button_layout)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def clear_text(self):
        self.text_edit.clear()

    def append_text(self):
        self.text_edit.append("Appended text!")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

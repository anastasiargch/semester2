from PyQt6.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QCheckBox, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGroupBox Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Создание QGroupBox
        group_box = QGroupBox("Options")
        group_box_layout = QVBoxLayout()

        # Добавление чекбоксов в QGroupBox
        checkbox1 = QCheckBox("Option 1")
        checkbox2 = QCheckBox("Option 2")
        checkbox3 = QCheckBox("Option 3")
        group_box_layout.addWidget(checkbox1)
        group_box_layout.addWidget(checkbox2)
        group_box_layout.addWidget(checkbox3)

        group_box.setLayout(group_box_layout)
        layout.addWidget(group_box)
        group_box.setCheckable(True)
        group_box.toggled.connect(self.group_box_toggled)
        # Создание контейнера для основного виджета
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def group_box_toggled(self, state):
        print(state)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
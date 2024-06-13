from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QRadioButton, QWidget, QButtonGroup, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRadioButton Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Создание QRadioButton
        self.radio_button1 = QRadioButton("Option 1")
        self.radio_button2 = QRadioButton("Option 2")
        self.radio_button3 = QRadioButton("Option 3")

        # Группировка радиокнопок
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button1)
        self.button_group.addButton(self.radio_button2)
        self.button_group.addButton(self.radio_button3)

        # Подключение сигналов
        self.radio_button1.toggled.connect(self.on_radio_button_toggled)
        self.radio_button2.toggled.connect(self.on_radio_button_toggled)
        self.radio_button3.toggled.connect(self.on_radio_button_toggled)

        # Добавление радиокнопок в компоновку
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(self.radio_button3)

        # Метка для отображения выбранного варианта
        self.label = QLabel("Selected: None")
        layout.addWidget(self.label)

        # Создание контейнера для основного виджета
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_radio_button_toggled(self):
        selected_button = self.button_group.checkedButton()
        if selected_button:
            self.label.setText(f"Selected: {selected_button.text()}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSpinBox, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Создание метки для отображения значений спин-бокса
        self.label = QLabel("Value: 0")
        layout.addWidget(self.label)

        # Создание спин-бокса
        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 100)
        self.spin_box.setSingleStep(1)
        self.spin_box.valueChanged.connect(self.on_value_changed)
        layout.addWidget(self.spin_box)

        # Создание контейнера для основного виджета
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_value_changed(self, value):
        self.label.setText(f"Value: {value}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

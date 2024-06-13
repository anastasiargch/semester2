from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QScrollBar, QWidget, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QScrollBar Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Создание метки для отображения значений прокрутки
        self.label = QLabel("Value: 0")
        layout.addWidget(self.label)

        # Создание вертикальной полосы прокрутки
        self.v_scrollbar = QScrollBar(Qt.Orientation.Vertical)
        self.v_scrollbar.setRange(0, 100)
        self.v_scrollbar.setSingleStep(1)
        self.v_scrollbar.setPageStep(10)
        self.v_scrollbar.valueChanged.connect(self.on_value_changed)
        layout.addWidget(self.v_scrollbar)

        # Создание горизонтальной полосы прокрутки
        self.h_scrollbar = QScrollBar(Qt.Orientation.Horizontal)
        self.h_scrollbar.setRange(0, 100)
        self.h_scrollbar.setSingleStep(1)
        self.h_scrollbar.setPageStep(10)
        self.h_scrollbar.valueChanged.connect(self.on_value_changed)
        layout.addWidget(self.h_scrollbar)

        # Создание контейнера для основного виджета
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_value_changed(self):
        value = self.sender().value()
        self.label.setText(f"Value: {value}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

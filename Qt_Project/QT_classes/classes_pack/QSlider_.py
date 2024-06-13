from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider, QWidget, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Создание метки для отображения значений ползунка
        self.label = QLabel("Value: 0")
        layout.addWidget(self.label)

        # Создание горизонтального ползунка
        self.h_slider = QSlider(Qt.Orientation.Horizontal)
        self.h_slider.setRange(0, 100)
        self.h_slider.setSingleStep(1)
        self.h_slider.setPageStep(10)
        self.h_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.h_slider.setTickInterval(10)
        self.h_slider.valueChanged.connect(self.on_value_changed)
        layout.addWidget(self.h_slider)

        # Создание вертикального ползунка
        self.v_slider = QSlider(Qt.Orientation.Vertical)
        self.v_slider.setRange(0, 100)
        self.v_slider.setSingleStep(1)
        self.v_slider.setPageStep(10)
        self.v_slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        self.v_slider.setTickInterval(10)
        self.v_slider.valueChanged.connect(self.on_value_changed)
        layout.addWidget(self.v_slider)

        # Создание контейнера для основного виджета
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_value_changed(self):
        sender = self.sender()
        value = sender.value()
        self.label.setText(f"Value: {value}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

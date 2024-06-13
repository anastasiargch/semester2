from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Создание QListWidget
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Item 1", "Item 2", "Item 3"])
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        layout.addWidget(self.list_widget)

        # Создание контейнера для основного виджета
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_item_clicked(self, item):
        QMessageBox.information(self, "Item Clicked", f"You clicked: {item.text()}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

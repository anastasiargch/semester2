from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTableWidget Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Создание таблицы
        self.table = QTableWidget(3, 3)  # 3 строки и 3 столбца
        self.table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        self.table.setVerticalHeaderLabels(["Row 1", "Row 2", "Row 3"])

        # Заполнение таблицы
        for row in range(3):
            for column in range(3):
                item = QTableWidgetItem(f"Item {row+1}, {column+1}")
                self.table.setItem(row, column, item)

        # Обработка изменения ячейки
        self.table.itemChanged.connect(self.on_item_changed)

        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_item_changed(self, item):
        print(f"Item changed: {item.text()} at row {item.row()}, column {item.column()}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

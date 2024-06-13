from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Создание виджета вкладок
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        # Создание вкладок
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout()
        self.tab1_layout.addWidget(QLabel("Content of Tab 1"))
        self.tab1.setLayout(self.tab1_layout)
        self.tabs.addTab(self.tab1, "Tab 1")

        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout()
        self.tab2_layout.addWidget(QLabel("Content of Tab 2"))
        self.tab2.setLayout(self.tab2_layout)
        self.tabs.addTab(self.tab2, "Tab 2")

        layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def close_tab(self, index):
        self.tabs.removeTab(index)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

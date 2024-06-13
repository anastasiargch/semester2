from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QLineEdit Constructors")
        self.resize(300, 100)
        # Line edit with a parent widget
        self.top_line_edit = QLineEdit(parent=self)
        # Line edit with a parent widget and a default text
        self.bottom_line_edit = QLineEdit(
            "Hello! This is a line edit.", parent=self
        )
        self.top_line_edit.editingFinished.connect(self.text_changed)
        layout = QVBoxLayout()
        layout.addWidget(self.top_line_edit)
        layout.addWidget(self.bottom_line_edit)
        self.setLayout(layout)

    def text_changed(self):
        print(self.top_line_edit.displayText())

app = QApplication([])
window = Window()
window.show()
app.exec()
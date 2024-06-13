import sys

from PyQt6.QtWidgets import QMainWindow, QCheckBox, QApplication
from PyQt6.QtCore import Qt
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked.value)
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

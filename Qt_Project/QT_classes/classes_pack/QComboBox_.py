import sys

from PyQt6.QtWidgets import QMainWindow, QComboBox, QApplication
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three", 'Four'])

        # Sends the current index (position) of the selected item.
        widget.currentIndexChanged.connect( self.index_changed )

        # There is an alternate signal to send the text.
        widget.currentTextChanged.connect( self.text_changed )

        self.setCentralWidget(widget)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec())
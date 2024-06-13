from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QRect

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPainter Example")
        self.setGeometry(100, 100, 400, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShapes(painter)

    def drawShapes(self, painter):
        # Установка пера и кисти
        pen = QPen(QColor(0, 0, 255), 2, Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        brush = QBrush(QColor(0, 255, 0, 128))
        painter.setBrush(brush)

        # Рисование примитивов
        painter.drawLine(10, 10, 100, 100)
        painter.drawRect(120, 10, 80, 60)
        painter.drawEllipse(220, 10, 80, 60)
        painter.drawText(10, 200, "Hello, QPainter!")

app = QApplication([])
window = DrawingWidget()
window.show()
app.exec()

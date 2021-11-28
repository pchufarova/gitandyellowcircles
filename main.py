from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
from random import randint


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.dopaint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.dopaint = True
        self.repaint()

    def paintEvent(self, event):
        if self.dopaint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(0, 300)
        qp.drawEllipse(randint(10, 560), randint(10, 470), x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QScreen
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import QPushButton, QColorDialog, QInputDialog
from design import Ui_MainWindow
from PIL import Image


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = 0
        self.y = 0
        self.my_brash = 5
        self.color = QColor(255, 255, 255)
        self.coords = []
        self.left_color.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.black_c.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.blue_c.setStyleSheet("background-color: rgb(0, 0, 255)")
        self.brown_c.setStyleSheet("background-color: rgb(165, 42, 42)")
        self.red_c.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.green_c.setStyleSheet("background-color: rgb(0, 255, 0)")
        self.grey_c.setStyleSheet("background-color: rgb(128, 128, 128)")
        self.white_c.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.yellow_c.setStyleSheet("background-color: rgb(255, 255, 0)")

        self.brash.activated[str].connect(self.onActivated)
        self.grab_btn.clicked.connect(self.save_image)
        self.clean.clicked.connect(self.clean_im)
        self.black_c.clicked.connect(self.run)
        self.blue_c.clicked.connect(self.run)
        self.brown_c.clicked.connect(self.run)
        self.red_c.clicked.connect(self.run)
        self.green_c.clicked.connect(self.run)
        self.grey_c.clicked.connect(self.run)
        self.white_c.clicked.connect(self.run)
        self.yellow_c.clicked.connect(self.run)
        self.collor_settings.clicked.connect(self.run1)

    def run(self):
        color = self.sender().styleSheet()[22:-1].split(sep=', ')
        self.color = QColor(int(color[0]), int(color[1]), int(color[2]))
        self.left_color.setStyleSheet(self.sender().styleSheet())

    def clean_im(self):
        pass

    def run1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.left_color.setStyleSheet(
                "background-color: {}".format(color.name())
            )
        self.color = QColor(color.name())

    def save_image(self):
        pass

    def mouseMoveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

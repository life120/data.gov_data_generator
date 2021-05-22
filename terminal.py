# https://zetcode.com/gui/pyqt5/layout/
import sys
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("Ok")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)

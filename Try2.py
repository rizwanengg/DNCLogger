import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

class MainScreen(QDialog):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.sendBtn.clicked.connect(self.on_sendBtn.clicked)
    @pyqtSlot()
    def on_sendBtn_clicked(self):
        self.fileDisplay.addItem("Send Button Clicked")
        QMessageBox.information(self, "ListWidget", "You clicked send button: ")

Form, Window = uic.loadUiType("MainScreen.ui")


def window():
    app = QApplication(sys.argv)
    w = MainScreen()
    w.show()
    sys.exit(app.exec_())
#if __name__ == '__main__':
window()

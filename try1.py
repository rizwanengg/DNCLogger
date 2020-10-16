import sys
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox,
                             QApplication, QVBoxLayout)


class XFileDialog():

    def __init__(self):
        QtWidgets.QFileDialog.__init__(self)
        self.setDirectory(progdir)

    def setVisible(self,v):

        super(XFileDialog, self).setVisible(v)
        self.setAcceptMode(0)
        self.setFileMode(1)
        self.setFocusPolicy(11)
        self.setNameFilter("All (*) ;; FITS (*.fts *.fits *.new)")
        self.focusPreviousChild()


class MyWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        super().__init__()

        self.initUI()

    def openFile(self):
        global progdir
        progdir=QtCore.QDir(os.getcwd())
        file=XFileDialog()
        file.exec()
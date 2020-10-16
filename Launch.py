import sys
import time
import easygui

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi
from FileSend import detectPort


import tkinter as tk
from tkinter import filedialog
from MsgBoxTut import showdialog
from ReadFile import openFile
#FILE_LIMIT = 100
#RATE_OF_CHANGE = 1


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.initUI()
        self.sendBtn.clicked.connect(self.on_sendBtn1_clicked)
        self.pauseBtn.clicked.connect(self.on_pauseBtn1_clicked)
        self.resumeBtn.clicked.connect(self.on_resumeBtn1_clicked)
        self.abortBtn.clicked.connect(self.on_abortBtn1_clicked)
        self.restartBtn.clicked.connect(self.on_restartBtn1_clicked)
        self.backBtn.clicked.connect(self.on_backBtn1_clicked)
        list_of_ports = detectPort()
        print(list_of_ports)
    def initUI(self):
        loadUi('MainScreen.ui', self)

    def on_sendBtn1_clicked(self):
        print("Send Btn Clicked")
        file_path_string = ""
        try:
            self.displayFile()
        except(Exception):
            print("No file choosen")

    def displayFile(self):
        file_path_string = easygui.fileopenbox(msg="Select single file at a time.", title="Choose",
                                               default='C:/Users/CC Server3/PycharmProjects/GUIPractice/CodeFiles/*.*',
                                               filetypes=None, multiple=False)
        file_path_string = (file_path_string.replace('\\', "/"))
        x = file_path_string.split("/")
        l = len(x)

        file_path = "C:/Users/CC Server3/PycharmProjects/GUIPractice/CodeFiles/"+x[l - 1]
        print(file_path)

        fileptr = open(file_path, "r")


        #self.countLines(file_path)
        lineno = 0;

        while True:
              line = fileptr.readline()
              #QMessageBox.information(self, "Info", line)
              lineno += 1
              if not line:
                    break
              self.split_to_char(line)

                #write code to send char over COM port here
       #         self.onLineSent()
              fullline = "{}".format(lineno) + "  " + line.strip()
              self.addLineToFileDisplay(fullline)

            # showdialog()
        fileptr.close()
        #except(Exception):
     #   print("Display file error")

    def split_to_char (self,word):
   #     print(word)
#        print (len(word))
        for x in range(len(word)):
            ch=word[x]
            self.sendOverCOM(ch)
    #        print(ch)
        #return (word)

    def sendOverCOM(self,ch):
       # list_of_ports = self.detectPort()
      #  print(list_of_ports)
        print("..")



    def on_pauseBtn1_clicked(self):
        print("Pause Btn Clicked")

    def on_resumeBtn1_clicked(self):
        print("Resume Btn Clicked")

    def on_abortBtn1_clicked(self):
        print("Abort Btn Clicked")

    def on_restartBtn1_clicked(self):
        print("Restart Btn Clicked")

    def on_backBtn1_clicked(self):
        print("back Btn Clicked")

    def addLineToFileDisplay(self,line):
        self.fileDisplay.addItem(line)

def window():
    app = QApplication(sys.argv)
    w = MainScreen()
    w.show()
    sys.exit(app.exec_())
#if __name__ == '__main__':
window()

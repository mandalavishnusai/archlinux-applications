#!/usr/bin/env python3


import sys
import os
import subprocess
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class shutdown(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shutdown")
        self.setGeometry(700,400,700,300)
        self.setFixedWidth(700)
        self.setFixedHeight(300)


        self.UiComponents()
        self.show()

    def UiComponents(self):
        self.label_1=QLabel("RudraOS",self)
        self.label_1.move(220,35)
        self.label_1.setFont(QFont('Arial', 47))
        self.label_1.resize(450,80)
        self.label_2 = QLabel('what do you want the computer to do?', self)
        self.label_2.move(150,130)
        self.label_2.resize(250, 20)
        self.combo_box=QComboBox(self)
        self.combo_box.setGeometry(150,170,420,30)

        shutdown_list = ["Shutdown", "Restart", "Logout"]

        self.combo_box.addItems(shutdown_list)
        self.combo_box.setEditable(False)

        button = QPushButton("OK",self)
        button.move(400,240)
        quitbutton = QPushButton("Cancel",self)
        quitbutton.move(520,240)
        quitbutton.clicked.connect(self.close)
        print(self.combo_box.count())
        button.pressed.connect(self.find)
        self.label=QLabel(self)
        self.label.setGeometry(200,200,200,30)

    def find(self):
        index = self.combo_box.currentIndex()

        '''self.label.setText(str(index))'''

        if index==0:
            print(subprocess.run(["poweroff"]))
            exit()

        if index==1:
            print(subprocess.run(["qdbus","org.kde.ksmserver","/KSMServer","logout","0","1","3"]))
            exit()

        if index==2:
            print(subprocess.run(["qdbus","org.kde.ksmserver","/KSMServer","logout","0","0","3"]))
            exit()





App = QApplication(sys.argv)
shutdown = shutdown()
sys.exit(App.exec())

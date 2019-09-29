import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from calc import Calculator

class Window(QWidget):

    liste = ["+","-","/","*","1","2","3","AC","4","5","6","0","7","8","9","="]
    extraOperator = ["+/-","=","AC"]

    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUI()

    def setupUI(self):
        
        self.setWindowTitle("Taschenrechner")
        self.resize(280,300)

        gridLayout = QGridLayout()
        gridLayout.setGeometry(QRect(20,80,240,220))
        gridLayout.setObjectName("gridBase")
        gridLayout.setContentsMargins(5,5,5,5)

        self.buttons = []
        c = 0; b = 0
        
        for _ in list(range(0,(4*4))):
            self.buttons.append(QPushButton(self.liste[_]))
            self.buttons[_].setObjectName("pushbutton" + str(_))
            self.buttons[_].clicked.connect(self.triggerClick)

            if c >= 4: c = 0; b += 1
            self.buttons[_].setText(self.liste[_])
            gridLayout.addWidget(self.buttons[_],b + 1,c,1,1)
           
            c += 1
        
        self.textLine = QLineEdit("")
        self.textLine.setAttribute(Qt.WA_MacShowFocusRect,0)
        self.textLine.textEdited.connect(self.onlyDefined)

        gridLayout.addWidget(self.textLine,0,0,1,4)

        self.setLayout(gridLayout)
        self.setStyleSheet(open("calc.css","r").read())
 
        self.show()

    def triggerClick(self):
        sender = self.sender()

        if sender.text() in self.liste and not (self.textLine.text()[-1:] in ["+","-","*","/"] and sender.text() in ["+","-","*","/"]):
            if sender.text() in self.extraOperator:
                self.clearAC(sender.text())
                self.calc(sender.text())
            else:
                self.textLine.setText(self.textLine.text()  + sender.text())


    def onlyDefined(self, e):

        if e[-1:] in self.liste and not (e[-2:-1] in ["+","-","*","/"] and e[-1:] in ["+","-","*","/"]):
            if e[-1:] in self.extraOperator:
                self.clearAC(e[-1:])
                self.calc(e[-1:])
            else:
                self.textLine.setText(e)    
        else:
            self.textLine.setText(e[:-1])

    def clearAC(self,i):
        if i == 'AC':
            self.textLine.setText("")


    def calc(self,i):
        self.setWindowTitle("Calculator")

        if i == "=":
            formel = self.textLine.text().replace("=","")

            clc = Calculator()
            try:
                r = clc.worker(formel)
            except ZeroDivisionError as ident:
                r = ""
                self.setWindowTitle("Zero Divison Error")


            self.textLine.setText(str(r))

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            self.calc("=")



app = QApplication(sys.argv)

w = Window()

sys.exit(app.exec_())

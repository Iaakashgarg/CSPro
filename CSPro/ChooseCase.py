from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import Choose
import random


#CASE SCREEN FOR POPULATION
class ChooseCase1(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(" Graphical Analysis Section!!! ")
        self.setGeometry(400, 100, 1000, 700)
        grid = QGridLayout()

        newfont = QFont("Arial", 18, QFont.Bold)
        label1 = QLabel("Please Choose Any Option To Proceed!!!")
        label1.setFont(newfont)

        btn1 = QPushButton("View Population of Single Year")
        btn2 = QPushButton("View Year Wise Population Graph")
        btn3 = QPushButton("View Population Graph of two Countries")
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)
        grid.addWidget(label1, 0, 0, 1, 4)
        grid.addWidget(btn1, 1, 0, 1, 4)
        grid.addWidget(btn2, 3, 0, 1, 4)
        grid.addWidget(btn3, 5, 0, 1, 4)

        btn1.clicked.connect(self.perform1)
        btn2.clicked.connect(self.perform2)
        btn3.clicked.connect(self.perform3)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        try :
            ob = Choose.ChooseCase1()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)

    def perform2(self):
        try :
            ob = Choose.ChooseCase4()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)

    def perform3(self):
        try :
            ob = Choose.ChooseCase7()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)


#CASE SCREEN FOR FERTILITY RATE
class ChooseCase2(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(" Graphical Analysis Section!!! ")
        self.setGeometry(400, 100, 1000, 700)
        grid = QGridLayout()

        newfont = QFont("Arial", 18, QFont.Bold)
        label1 = QLabel("Please Choose Any Option To Proceed!!!")
        label1.setFont(newfont)

        btn1 = QPushButton("View Fertility Rate of Single Year")
        btn2 = QPushButton("View Year Wise Fertility Rate Graph")
        btn3 = QPushButton("View Fertility Rate Graph of two Countries")
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)
        grid.addWidget(label1, 0, 0, 1, 4)
        grid.addWidget(btn1, 1, 0, 1, 4)
        grid.addWidget(btn2, 3, 0, 1, 4)
        grid.addWidget(btn3, 5, 0, 1, 4)

        btn1.clicked.connect(self.perform1)
        btn2.clicked.connect(self.perform2)
        btn3.clicked.connect(self.perform3)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)

        self.setLayout(grid)

        self.show()


    def perform1(self):
        try :
            ob = Choose.ChooseCase2()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)

    def perform2(self):
        try :
            ob = Choose.ChooseCase5()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)

    def perform3(self):
        try :
            ob = Choose.ChooseCase8()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)

# CASE SCREEN FOR LIFE EXPECTANCY
class ChooseCase3(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(" Graphical Analysis Section!!! ")
        self.setGeometry(400, 100, 1000, 700)
        grid = QGridLayout()

        newfont = QFont("Arial", 18, QFont.Bold)
        label1 = QLabel("Please Choose Any Option To Proceed!!!")
        label1.setFont(newfont)

        btn1 = QPushButton("View Life Expectancy of Single Year")
        btn2 = QPushButton("View Year Wise Life Expectancy Graph")
        btn3 = QPushButton("View Life Expectancy Graph of two Countries")
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)
        grid.addWidget(label1, 0, 0, 1, 4)
        grid.addWidget(btn1, 1, 0, 1, 4)
        grid.addWidget(btn2, 3, 0, 1, 4)
        grid.addWidget(btn3, 5, 0, 1, 4)

        btn1.clicked.connect(self.perform1)
        btn2.clicked.connect(self.perform2)
        btn3.clicked.connect(self.perform3)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)

        self.setLayout(grid)

        self.show()


    def perform1(self):
        try :
            ob = Choose.ChooseCase3()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)

    def perform2(self):
        try :
            ob = Choose.ChooseCase6()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)

    def perform3(self):
        try :
            ob = Choose.ChooseCase9()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)


class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)

        qp.setPen(Qt.darkBlue)
        size = self.size()

        for i in range(1024):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChooseCase1()
    sys.exit(app.exec_())
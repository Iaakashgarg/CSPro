from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pandas as pd
import LiveDetails
import CompareScreen


class LiveScreen(QWidget):
    def __init__(self,parent=None):
        super(LiveScreen, self).__init__()
        self.parent=parent
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label1.setFont(newfont)

        btn1 = QPushButton("Show Current Population")
        btn1.setFont(newfont)
        btn2 = QPushButton("Show Expected Population(2030)")
        btn2.setFont(newfont)
        btn3 = QPushButton("Show Expected Population(2050)")
        btn3.setFont(newfont)

        self.combo1 = QComboBox()

        df = LiveDetails.func()
        countries = df["Country Name"].tolist()

        self.combo1.addItems(countries)
        self.combo1.setFont(newfont)

        btn1.clicked.connect(self.perform1)
        btn2.clicked.connect(self.perform2)
        btn3.clicked.connect(self.perform3)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(btn1, 3, 0, 1, 4)
        grid.addWidget(btn2, 4, 0, 1, 4)
        grid.addWidget(btn3, 5, 0, 1, 4)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = CompareScreen.PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        try:
            country = self.combo1.currentText()
            ob = Numeric1(country,self)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

    def perform2(self):
        try:
            country = self.combo1.currentText()
            ob = Numeric2(country,self)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

    def perform3(self):
        try:
            country = self.combo1.currentText()
            ob = Numeric3(country,self)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

class LiveScreen2(QWidget):
    def __init__(self,parent=None):
        super(LiveScreen2, self).__init__()
        self.parent=parent
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label1.setFont(newfont)

        btn1 = QPushButton("Show Population Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()

        df = LiveDetails.func()
        countries = df["Country Name"].tolist()
        self.combo1.addItems(countries)
        self.combo1.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(btn1, 3, 0, 1, 4)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = CompareScreen.PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country = self.combo1.currentText()
        LiveDetails.MainGraph(self, country)

class LiveScreen3(QWidget):
    def __init__(self,parent=None):
        super(LiveScreen3, self).__init__()
        self.parent=parent
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label1.setFont(newfont)

        btn1 = QPushButton("Show Growth Rate")
        btn1.setFont(newfont)
        btn2 = QPushButton("Show Rank")
        btn2.setFont(newfont)

        self.combo1 = QComboBox()

        df = LiveDetails.func()
        countries = df["Country Name"].tolist()

        self.combo1.addItems(countries)
        self.combo1.setFont(newfont)

        btn1.clicked.connect(self.perform1)
        btn2.clicked.connect(self.perform2)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(btn1, 3, 0, 1, 4)
        grid.addWidget(btn2, 4, 0, 1, 4)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = CompareScreen.PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)


        self.setLayout(grid)
        self.show()

    def perform1(self):
        try:
            country = self.combo1.currentText()
            ob = GrowthRate(country,self)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

    def perform2(self):
        try:
            country = self.combo1.currentText()
            ob = Rank(country,self)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

class Numeric1(QDialog ):
    try:
        def __init__(self,country,parent=None):
            self.country = country
            self.parent = parent
            super(Numeric1, self).__init__()
            grid = QGridLayout()
            newfont = QFont("Comic Sans MS", 24, QFont.Bold)

            label1 = QLabel("Current Population of " + self.country )
            label1.move(50,50)
            label1.setFont(newfont)

            self.df2 = LiveDetails.func()
            print(self.df2)
            dq = self.df2[self.df2["Country Name"] == self.country]["Current Population"].item()
            print(dq)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(dq)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            msg.setFont(newfont)

            grid.addWidget(label1)
            grid.addWidget(msg)
            self.setLayout(grid)
            self.show()

    except BaseException as ex:
        print(ex)


class Numeric2(QDialog ):
    def __init__(self,country,parent=None):
        self.country = country
        self.parent = parent
        super(Numeric2, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel("Expected Population of " + self.country + " In 2030" )
        label1.move(50,50)
        label1.setFont(newfont)

        df = LiveDetails.func()
        dq = df[df["Country Name"] == self.country]["Expected Population"].item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(dq)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.setFont(newfont)

        grid.addWidget(label1)
        grid.addWidget(msg)

        self.setLayout(grid)
        self.show()


class Numeric3(QDialog ):
    def __init__(self,country,parent=None):
        self.country = country
        self.parent = parent
        super(Numeric3, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel("Expected Population of " + self.country + " In 2050")
        label1.move(50,50)
        label1.setFont(newfont)

        df = LiveDetails.func()
        dq = df[df["Country Name"] == self.country]["New Population"].item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(dq)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.setFont(newfont)

        grid.addWidget(label1)
        grid.addWidget(msg)

        self.setLayout(grid)
        self.show()

class GrowthRate(QDialog ):
    def __init__(self,country,parent=None):
        self.country = country
        self.parent = parent
        super(GrowthRate, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel("Growth Rate of " + self.country )
        label1.move(50,50)
        label1.setFont(newfont)

        df = LiveDetails.func()
        dq = df[df["Country Name"] == self.country]["Growth Rate"].item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(dq)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.setFont(newfont)

        grid.addWidget(label1)
        grid.addWidget(msg)

        self.setLayout(grid)
        self.show()

class Rank(QDialog ):
    def __init__(self,country,parent=None):
        self.country = country
        self.parent = parent
        super(Rank, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel("Rank of " + self.country + " in World ")
        label1.move(50,50)
        label1.setFont(newfont)

        df = LiveDetails.func()
        dq = df[df["Country Name"] == self.country]["Rank"].item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(dq)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setFont(newfont)
        grid.addWidget(label1)
        grid.addWidget(msg)
        self.setLayout(grid)
        self.show()

class World(QDialog ):
    def __init__(self,parent=None):
        self.parent = parent
        super(World, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel("2018 World Population " )
        label1.move(50,50)
        label1.setFont(newfont)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("7,632,819,325")
        msg.setStandardButtons(QMessageBox.NoButton)
        msg.setFont(newfont)
        grid.addWidget(label1)
        grid.addWidget(msg)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = CompareScreen.PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)

        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LiveScreen()
    sys.exit(app.exec_())
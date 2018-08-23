from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import NumericResults
import Graphs
import random

class General1(QDialog) :
    def __init__(self,parent=None):
        super(General1, self).__init__()
        self.parent = parent
        grid = QGridLayout()
        self.setWindowTitle("Census Comparison Analysis Section!!! ")
        self.setGeometry(400, 100, 1000, 700)
        newfont = QFont("Arial", 18, QFont.Bold)
        label1 = QLabel("Please Choose Any Option on Which Comparison has to be Done!!!")
        label1.setFont(newfont)

        btn1 = QPushButton("Comparison Between Two Countries in Single Year")
        btn2 = QPushButton("Comparison Among Two Years")
        btn3 = QPushButton("Compare Country VS Country")
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)
        grid.addWidget(label1, 0, 0, 1, 4)
        grid.addWidget(btn1, 1, 0, 1, 4)
        grid.addWidget(btn2, 3, 0, 1, 4)
        grid.addWidget(btn3, 4, 0, 1, 4)

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

    def perform1(self):
        try:
            ob = Compare1()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)


    def perform2(self):
        try:
            ob = Compare4()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

    def perform3(self):
        try:
            ob = Compare7()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)


class General2(QDialog):
    def __init__(self,parent=None):
        super(General2, self).__init__()
        self.parent = parent
        grid = QGridLayout()
        self.setWindowTitle("Fertility Rate Comparison Analysis Section!!! ")
        self.setGeometry(400, 100, 1000, 700)
        newfont = QFont("Arial", 18, QFont.Bold)
        label1 = QLabel("Please Choose Any Option on Which Comparison has to be Done!!!")
        label1.setFont(newfont)

        btn1 = QPushButton("Comparison Between Two Countries in Single Year")
        btn2 = QPushButton("Comparison Among Two Years")
        btn3 = QPushButton("Compare Country VS Country")
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)
        grid.addWidget(label1, 0, 0, 1, 4)
        grid.addWidget(btn1, 1, 0, 1, 4)
        grid.addWidget(btn2, 3, 0, 1, 4)
        grid.addWidget(btn3, 4, 0, 1, 4)

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

    def perform1(self):
        try:
            ob = Compare2()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

    def perform2(self):
        try:
            ob = Compare5()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

    def perform3(self):
        try:
            ob = Compare8()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)


class General3(QDialog):
    def __init__(self,parent=None):
        super(General3, self).__init__()
        self.parent = parent
        grid = QGridLayout()
        self.setWindowTitle("Life Expectancy Comparison Analysis Section!!! ")
        self.setGeometry(400, 100, 1000, 700)
        newfont = QFont("Arial", 18, QFont.Bold)
        label1 = QLabel("Please Choose Any Option on Which Comparison has to be Done!!!")
        label1.setFont(newfont)

        btn1 = QPushButton("Comparison Between Two Countries in Single Year")
        btn2 = QPushButton("Comparison Among Two Years")
        btn3 = QPushButton("Compare Country VS Country")
        btn1.setFont(newfont)
        btn2.setFont(newfont)
        btn3.setFont(newfont)
        grid.addWidget(label1, 0, 0, 1, 4)
        grid.addWidget(btn1, 1, 0, 1, 4)
        grid.addWidget(btn2, 3, 0, 1, 4)
        grid.addWidget(btn3, 4, 0, 1, 4)

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

    def perform1(self):
        try:
            ob = Compare3()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)

    def perform2(self):
        try:
            ob = Compare6()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)


    def perform3(self):
        try:
            ob = Compare9()
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
            print(ex)


class Case1(QWidget):
    def __init__(self):
        super(Case1, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label3 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)
        label3.setFont(newfont)

        btn1 = QPushButton("Compare Population")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo3 = QComboBox()

        data = pd.read_csv("country_population.csv")

        years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]

        self.countries = data["Country Name"]
        self.combo1.addItem("Choose Any Country")
        self.combo2.addItem("Choose Any Country")
        self.combo1.addItems(self.countries)
        self.combo3.addItems(years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        self.combo1.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(label3, 3, 0, 1, 3)
        grid.addWidget(self.combo3, 3, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pu.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo2.clear()
        self.combo2.addItem("Choose Any Country")
        if index != 0:
            for country in self.countries:
                if country != self.countries[index - 1]:
                    self.combo2.addItem(country)

    def perform1(self):
        try:
            if(self.combo1.currentIndex()==0 or self.combo2.currentIndex()==0):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country1 = self.combo1.currentText()
                country2 = self.combo2.currentText()
                year = self.combo3.currentText()
                Graphs.Graph1(self,country1,country2,year)
        except BaseException as ex:
            print(ex)

class Compare1(QMainWindow):
    def __init__(self):
        super(Compare1, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case1()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pu.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



class Case2(QDialog):
    def __init__(self):
        super(Case2, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Arial", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label3 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)
        label3.setFont(newfont)

        btn1 = QPushButton("Compare Fertility Rate")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo3 = QComboBox()

        data = pd.read_csv("fertility_rate.csv")
        years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]

        self.countries = data["Country Name"]
        self.combo1.addItem("Choose Any Country")
        self.combo2.addItem("Choose Any Country")
        self.combo1.addItems(self.countries)

        self.combo3.addItems(years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        self.combo1.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(label3, 3, 0, 1, 3)
        grid.addWidget(self.combo3, 3, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pu.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo2.clear()
        self.combo2.addItem("Choose Any Country")
        if index != 0:
            for country in self.countries:
                if country != self.countries[index - 1]:
                    self.combo2.addItem(country)

    def perform1(self):
        try:
            if(self.combo1.currentIndex()==0 or self.combo2.currentIndex()==0):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country1 = self.combo1.currentText()
                country2 = self.combo2.currentText()
                year = self.combo3.currentText()
                Graphs.Graph2(self, country1, country2, year)
        except BaseException as ex :
            print(ex)

class Compare2(QMainWindow):
    def __init__(self):
        super(Compare2, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case2()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pu.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



class Case3(QWidget):
    def __init__(self):
        super(Case3, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label3 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)
        label3.setFont(newfont)

        btn1 = QPushButton("Compare Life Expectancy")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo3 = QComboBox()

        data = pd.read_csv("life_expectancy.csv")

        years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]

        self.countries = data["Country Name"]
        self.combo1.addItem("Choose Any Country")
        self.combo2.addItem("Choose Any Country")
        self.combo1.addItems(self.countries)
        self.combo3.addItems(years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        self.combo1.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(label3, 3, 0, 1, 3)
        grid.addWidget(self.combo3, 3, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pu.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo2.clear()
        self.combo2.addItem("Choose Any Country")
        if index != 0:
            for country in self.countries:
                if country != self.countries[index - 1]:
                    self.combo2.addItem(country)


    def perform1(self):
        try:
            if(self.combo1.currentIndex()==0 or self.combo2.currentIndex()==0):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country1 = self.combo1.currentText()
                country2 = self.combo2.currentText()
                year = self.combo3.currentText()
                Graphs.Graph3(self, country1, country2, year)
        except BaseException as ex:
            print(ex)

class Compare3(QMainWindow):
    def __init__(self):
        super(Compare3, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case3()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pu.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



class Case4(QWidget):
    def __init__(self):
        super(Case4, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label3 = QLabel("Choose Another Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)
        label3.setFont(newfont)

        btn1 = QPushButton("Compare Population")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo3 = QComboBox()

        data = pd.read_csv("country_population.csv")

        self.years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]

        self.countries = data["Country Name"]

        self.combo1.addItems(self.countries)
        self.combo2.addItem("Choose Any Year")
        self.combo3.addItem("Choose Any Year")
        self.combo2.addItems(self.years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        self.combo2.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(label3, 3, 0, 1, 3)
        grid.addWidget(self.combo3, 3, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pu.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo3.clear()
        self.combo3.addItem("Choose Any Year")
        if index != 0:
            for year in self.years:
                if year != self.years[index - 1]:
                    self.combo3.addItem(year)

    def perform1(self):
        try:
            if(self.combo2.currentIndex()==0 or self.combo3.currentIndex()==0):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country = self.combo1.currentText()
                year1 = self.combo2.currentText()
                year2 = self.combo3.currentText()
                Graphs.Graph4(self, country, year1, year2)
        except BaseException as ex:
            print(ex)

class Compare4(QMainWindow):
    def __init__(self):
        super(Compare4, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case4()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pt.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



class Case5(QWidget):
    def __init__(self):
        super(Case5, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label3 = QLabel("Choose Another Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)
        label3.setFont(newfont)

        btn1 = QPushButton("Compare Fertility Rate")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo3 = QComboBox()

        data = pd.read_csv("fertility_rate.csv")

        self.years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
                      '1972', '1973', '1974',
                      '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                      '1987', '1988', '1989',
                      '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
                      '2002', '2003', '2004',
                      '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        self.countries = data["Country Name"]

        self.combo1.addItems(self.countries)
        self.combo2.addItem("Choose Any Year")
        self.combo3.addItem("Choose Any Year")
        self.combo2.addItems(self.years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        self.combo2.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(label3, 3, 0, 1, 3)
        grid.addWidget(self.combo3, 3, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pu.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo3.clear()
        self.combo3.addItem("Choose Any Year")
        if index != 0:
            for year in self.years:
                if year != self.years[index - 1]:
                    self.combo3.addItem(year)

    def perform1(self):
        try:
            if(self.combo2.currentIndex()==0 or self.combo3.currentIndex()==0 ):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country = self.combo1.currentText()
                year1 = self.combo2.currentText()
                year2 = self.combo3.currentText()
                Graphs.Graph5(self, country, year1, year2)
        except BaseException as ex:
            print(ex)


class Compare5(QMainWindow):
    def __init__(self):
        super(Compare5, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case5()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pt.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



class Case6(QWidget):
    def __init__(self):
        super(Case6, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label3 = QLabel("Choose Another Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)
        label3.setFont(newfont)

        btn1 = QPushButton("Compare Life Expectancy")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo3 = QComboBox()

        data = pd.read_csv("life_expectancy.csv")

        self.years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
                      '1972', '1973', '1974',
                      '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                      '1987', '1988', '1989',
                      '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
                      '2002', '2003', '2004',
                      '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        self.countries = data["Country Name"]

        self.combo1.addItems(self.countries)
        self.combo2.addItem("Choose Any Year")
        self.combo3.addItem("Choose Any Year")
        self.combo2.addItems(self.years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo3.setFont(newfont)
        self.combo2.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(label3, 3, 0, 1, 3)
        grid.addWidget(self.combo3, 3, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pu.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo3.clear()
        self.combo3.addItem("Choose Any Year")
        if index != 0:
            for year in self.years:
                if year != self.years[index - 1]:
                    self.combo3.addItem(year)

    def perform1(self):
        try:
            if(self.combo2.currentIndex()==0 or self.combo3.currentIndex()==0 ):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country = self.combo1.currentText()
                year1 = self.combo2.currentText()
                year2 = self.combo3.currentText()
                Graphs.Graph6(self, country, year1, year2)
        except BaseException as ex:
            print(ex)

class Compare6(QMainWindow):
    def __init__(self):
        super(Compare6, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case6()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pt.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



class Case7(QWidget):
    def __init__(self):
        super(Case7, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Compare Population")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("country_population.csv")


        self.countries = data["Country Name"]
        self.combo1.addItem("Choose Country")
        self.combo2.addItem("Choose Country")
        self.combo1.addItems(self.countries)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo1.currentIndexChanged.connect(self.changeValues)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo2.clear()
        self.combo2.addItem("Choose Country")
        if index != 0:
            for country in self.countries:
                if country != self.countries[index - 1]:
                    self.combo2.addItem(country)

    def perform1(self):
        try:
            if(self.combo1.currentIndex()==0 or self.combo2.currentIndex()==0):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country1 = self.combo1.currentText()
                country2 = self.combo2.currentText()
                Graphs.Graph7(self, country1, country2)
        except BaseException as ex :
            print(ex)

class Compare7(QMainWindow):
    def __init__(self):
        super(Compare7, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case7()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())




class Case8(QWidget):
    def __init__(self):
        super(Case8, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Compare Fertility Rate")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("fertility_rate.csv")

        self.countries = data["Country Name"]
        self.combo1.addItem("Choose Country")
        self.combo2.addItem("Choose Country")
        self.combo1.addItems(self.countries)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo1.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo2.clear()
        self.combo2.addItem("Choose Country")
        if index != 0:
            for country in self.countries:
                if country != self.countries[index - 1]:
                    self.combo2.addItem(country)


    def perform1(self):
        try:
            if(self.combo1.currentIndex()==0 or self.combo2.currentIndex()==0):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)

            else:
                country1 = self.combo1.currentText()
                country2 = self.combo2.currentText()
                Graphs.Graph8(self, country1, country2)
        except BaseException as ex :
            print(ex)

class Compare8(QMainWindow):
    def __init__(self):
        super(Compare8, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case8()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())




class Case9(QWidget):
    def __init__(self):
        super(Case9, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Compare Life Expectancy")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("life_expectancy.csv")

        self.countries = data["Country Name"]
        self.combo1.addItem("Choose Country")
        self.combo2.addItem("Choose Country")
        self.combo1.addItems(self.countries)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)
        self.combo1.currentIndexChanged.connect(self.changeValues)
        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 4, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def changeValues(self, index):
        self.combo2.clear()
        self.combo2.addItem("Choose Country")
        if index != 0:
            for country in self.countries:
                if country != self.countries[index - 1]:
                    self.combo2.addItem(country)



    def perform1(self):
        try:
            if(self.combo1.currentIndex()==0 or self.combo2.currentIndex()==0):
                QMessageBox.question(self, 'Warning!!', "Please Choose Valid Choice!",QMessageBox.NoButton)
            else:
                country1 = self.combo1.currentText()
                country2 = self.combo2.currentText()
                Graphs.Graph9(self, country1, country2)
        except BaseException as ex :
            print(ex)

class Compare9(QMainWindow):
    def __init__(self):
        super(Compare9, self).__init__()
        self.setWindowTitle(" Comparison Analysis Section!!! ")
        self._widget = Case9()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())

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
    ex = Compare2()
    sys.exit(app.exec_())



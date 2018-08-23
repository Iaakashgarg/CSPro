from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import NumericResults
import Graphs
import random


class ChooseScreen1(QWidget):
    def __init__(self):
        super(ChooseScreen1, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Population Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("country_population.csv")

        years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972',
                 '1973', '1974',
                 '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                 '1988', '1989',
                 '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                 '2003', '2004',
                 '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo2.addItems(years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 3, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country = self.combo1.currentText()
        year = self.combo2.currentText()
        Graphs.showGraph(self,country,year)

class ChooseCase1(QMainWindow):
    def __init__(self):
        super(ChooseCase1, self).__init__()
        self.setWindowTitle(" Population Graphical Analysis Section!!! ")
        self._widget = ChooseScreen1()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())




class ChooseScreen2(QWidget):
    def __init__(self):
        super(ChooseScreen2, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Fertility Rate Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("fertility_rate.csv")

        years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972',
                 '1973', '1974',
                 '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                 '1988', '1989',
                 '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                 '2003', '2004',
                 '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo2.addItems(years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 3, 0, 1, 4)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country = self.combo1.currentText()
        year = self.combo2.currentText()
        Graphs.showGraphFertility(self, country, year)

class ChooseCase2(QMainWindow):
    def __init__(self):
        super(ChooseCase2, self).__init__()
        self.setWindowTitle(" Fertility Rate Graphical Analysis Section!!! ")
        self._widget = ChooseScreen2()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


class ChooseScreen3(QWidget):
    def __init__(self):
        super(ChooseScreen3, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Life Expectancy Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("life_expectancy.csv")

        years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972',
                 '1973', '1974',
                 '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                 '1988', '1989',
                 '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                 '2003', '2004',
                 '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo2.addItems(years)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 3, 0, 1, 4)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country = self.combo1.currentText()
        year = self.combo2.currentText()
        Graphs.showGraphLife(self, country, year)


class ChooseCase3(QMainWindow):
    def __init__(self):
        super(ChooseCase3, self).__init__()
        self.setWindowTitle(" Life Expectancy Graphical Analysis Section!!! ")
        self._widget = ChooseScreen3()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



class ChooseScreen4(QWidget):
    def __init__(self):
        super(ChooseScreen4, self).__init__()
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 18, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label1.setFont(newfont)

        btn1 = QPushButton("Show Population Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()

        data = pd.read_csv("country_population.csv")

        years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972',
                 '1973', '1974',
                 '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                 '1988', '1989',
                 '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                 '2003', '2004',
                 '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo1.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(btn1, 3, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pw.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country = self.combo1.currentText()
        Graphs.viewGraphPopulation(self, country)

class ChooseCase4(QMainWindow):
    def __init__(self):
        super(ChooseCase4, self).__init__()
        self.setWindowTitle(" Population Graphical Analysis Section!!! ")
        self._widget = ChooseScreen4()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pw.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


class ChooseScreen5(QWidget):
    def __init__(self):
        super(ChooseScreen5, self).__init__()
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")

        label1.setFont(newfont)


        btn1 = QPushButton("Show Fertility Rate Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()

        data = pd.read_csv("fertility_rate.csv")

        years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972',
                 '1973', '1974',
                 '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                 '1988', '1989',
                 '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                 '2003', '2004',
                 '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo1.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(btn1, 3, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pw.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country = self.combo1.currentText()
        Graphs.viewGraphFertility(self, country)

class ChooseCase5(QMainWindow):
    def __init__(self):
        super(ChooseCase5, self).__init__()
        self.setWindowTitle(" Fertility Rate Graphical Analysis Section!!! ")
        self._widget = ChooseScreen5()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pw.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


class ChooseScreen6(QWidget):
    def __init__(self):
        super(ChooseScreen6, self).__init__()
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label1.setFont(newfont)

        btn1 = QPushButton("Show Life Expectancy Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()

        data = pd.read_csv("life_expectancy.csv")

        years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972',
                 '1973', '1974',
                 '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                 '1988', '1989',
                 '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                 '2003', '2004',
                 '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo1.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(btn1, 3, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pw.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country = self.combo1.currentText()
        Graphs.viewGraphLife(self, country)

class ChooseCase6(QMainWindow):
    def __init__(self):
        super(ChooseCase6, self).__init__()
        self.setWindowTitle(" Life Expectancy Graphical Analysis Section!!! ")
        self._widget = ChooseScreen6()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pw.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


class ChooseScreen7(QWidget):
    def __init__(self):
        super(ChooseScreen7, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Population Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("country_population.csv")

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo2.addItems(countries)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 3, 0, 1, 4)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country1 = self.combo1.currentText()
        country2 = self.combo2.currentText()
        Graphs.barGraph1(self,country1,country2)

class ChooseCase7(QMainWindow):
    def __init__(self):
        super(ChooseCase7, self).__init__()
        self.setWindowTitle(" Population Graphical Analysis Section!!! ")
        self._widget = ChooseScreen7()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())




class ChooseScreen8(QWidget):
    def __init__(self):
        super(ChooseScreen8, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Fertility Rate Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("fertility_rate.csv")


        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo2.addItems(countries)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 3, 0, 1, 4)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country1 = self.combo1.currentText()
        country2 = self.combo2.currentText()
        Graphs.barGraph2(self, country1, country2)

class ChooseCase8(QMainWindow):
    def __init__(self):
        super(ChooseCase8, self).__init__()
        self.setWindowTitle(" Fertility Rate Graphical Analysis Section!!! ")
        self._widget = ChooseScreen8()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


class ChooseScreen9(QWidget):
    def __init__(self):
        super(ChooseScreen9, self).__init__()
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Another Country : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Life Expectancy Graph")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("life_expectancy.csv")

        countries = data["Country Name"]

        self.combo1.addItems(countries)
        self.combo2.addItems(countries)
        self.combo1.setFont(newfont)
        self.combo2.setFont(newfont)

        btn1.clicked.connect(self.perform1)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(label2, 2, 0, 1, 3)
        grid.addWidget(self.combo2, 2, 1, 1, 3)
        grid.addWidget(btn1, 3, 0, 1, 4)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pp.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setLayout(grid)
        self.show()

    def perform1(self):
        country1 = self.combo1.currentText()
        country2 = self.combo2.currentText()
        Graphs.barGraph3(self, country1, country2)


class ChooseCase9(QMainWindow):
    def __init__(self):
        super(ChooseCase9, self).__init__()
        self.setWindowTitle(" Life Expectancy Graphical Analysis Section!!! ")
        self._widget = ChooseScreen9()
        self.setCentralWidget(self._widget)
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pp.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChooseScreen1()
    sys.exit(app.exec_())


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import NumericResults
import Graphs
import random

class ChooseNum1(QDialog):
    def __init__(self,parent=None):
        super(ChooseNum1, self).__init__()
        self.parent = parent
        self.setWindowTitle(" Welcome Buddy!!! ")
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Population")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("country_population.csv")

        years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]



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
            country = self.combo1.currentText()
            year = self.combo2.currentText()
            ob = NumericResults.Population(country,year,self.parent)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)





class ChooseNum2(QDialog):
    def __init__(self,parent=None):
        super(ChooseNum2, self).__init__()
        self.parent = parent
        self.setWindowTitle(" Welcome Buddy!!! ")
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Fertility Rate")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("fertility_rate.csv")

        years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]



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
            country = self.combo1.currentText()
            year = self.combo2.currentText()
            ob = NumericResults.Fertility(country,year,self.parent)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex :
            print(ex)





class ChooseNum3(QDialog):
    def __init__(self,parent=None):
        super(ChooseNum3, self).__init__()
        self.parent = parent
        self.setWindowTitle(" Welcome Buddy!!! ")
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()

        newfont = QFont("Comic Sans MS", 20, QFont.Bold)
        label1 = QLabel("Choose Any Country : ")
        label2 = QLabel("Choose Any Year : ")
        label1.setFont(newfont)
        label2.setFont(newfont)

        btn1 = QPushButton("Show Life Expectancy")
        btn1.setFont(newfont)

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        data = pd.read_csv("life_expectancy.csv")

        years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]



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
            country = self.combo1.currentText()
            year = self.combo2.currentText()
            ob = NumericResults.Life(country,year,self.parent)
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




'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChooseNum1()
    sys.exit(app.exec_())            '''



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys

data1 = pd.read_csv("country_population.csv")
data2 = pd.read_csv("fertility_rate.csv")
data3 = pd.read_csv("life_expectancy.csv")


class showPopulation(QDialog ):
    def __init__(self,country,year,parent=None):
        self.country = country
        self.year = year
        self.parent = parent
        super(showPopulation, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel(self.country + "'s Population in the Year " + self.year)
        label1.move(50,50)
        label1.setFont(newfont)

        disp = data1[data1["Country Name"] == self.country][self.year].item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(str(disp))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.setFont(newfont)

        grid.addWidget(label1)
        grid.addWidget(msg)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pio.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.setLayout(grid)
        self.show()


class Population(QMainWindow):
    def __init__(self,country,year,parent=None):
        super(Population, self).__init__()
        self.country = country
        self.year = year
        self.parent = parent

        self._widget = showPopulation(self.country,self.year,self.parent)
        self.setCentralWidget(self._widget)
        self.setWindowTitle(" Census Analysis!!! ")
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pio.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


class showFertility(QDialog):
    def __init__(self,country,year,parent=None):
        self.country = country
        self.year = year
        self.parent = parent
        super(showFertility, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel(self.country + "'s Fertility Rate in the Year " + self.year)
        label1.move(50, 50)
        label1.setFont(newfont)

        disp = data2[data2["Country Name"] == self.country][self.year].item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(str(disp))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.setFont(newfont)

        grid.addWidget(label1)
        grid.addWidget(msg)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pio.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.setLayout(grid)
        self.show()

class Fertility(QMainWindow):
    def __init__(self,country,year,parent=None):
        super(Fertility, self).__init__()
        self.country = country
        self.year = year
        self.parent = parent

        self._widget = showFertility(self.country,self.year,self.parent)
        self.setCentralWidget(self._widget)
        self.setWindowTitle(" Fertility Rate Analysis!!! ")
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pio.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


class showLife(QDialog):
    def __init__(self,country,year,parent=None):
        self.country = country
        self.year = year
        self.parent = parent
        super(showLife, self).__init__()
        grid = QGridLayout()
        newfont = QFont("Comic Sans MS", 24, QFont.Bold)

        label1 = QLabel(self.country + "'s Life Expectancy Rate in the Year " + self.year)
        label1.move(50, 50)
        label1.setFont(newfont)

        disp = data3[data3["Country Name"] == self.country][self.year].item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(str(disp))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.setFont(newfont)

        grid.addWidget(label1)
        grid.addWidget(msg)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pio.jpg")))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.setLayout(grid)
        self.show()

class Life(QMainWindow):
    def __init__(self,country,year,parent=None):
        super(Life, self).__init__()
        self.country = country
        self.year = year
        self.parent = parent

        self._widget = showLife(self.country,self.year,self.parent)
        self.setCentralWidget(self._widget)
        self.setWindowTitle(" Life Expectancy Analysis!!! ")
        self.setGeometry(100,70,425,346)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def resizeEvent(self, event):
        pixmap = QPixmap("pu.jpg")
        region = QRegion(pixmap.mask())
        self.setMask(pixmap.mask())


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = showPopulation()
    sys.exit(app.exec_())             '''
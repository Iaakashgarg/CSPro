from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import ChooseNum
import ChooseCase
import CompareScreen
import Countries
import LiveScreen

class MainScreen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        pix = QPixmap("qwert.jpg")

        pix2 = pix.scaled(QSize(1100,650))

        self.brush = QBrush(pix2)
        self.mdi.setBackground(self.brush)

        self.setWindowTitle(" Welcome To CSPro ")
        self.setGeometry(200, 70, 1100, 650)
        font = QFont("Comic Sans MS", 18, QFont.Bold)
        newfont = QFont("Comic Sans MS", 14, QFont.Bold)
        mainMenu = self.menuBar()
        menu1 = mainMenu.addMenu("Numeric Operations")
        menu2 = mainMenu.addMenu("Graphical Analysis")
        menu3 = mainMenu.addMenu("Comparison Analysis")
        menu4 = mainMenu.addMenu("Countries Operations")
        menu5 = mainMenu.addMenu("LIVE Details")
        mainMenu.setFont(newfont)
        menu1.setFont(font)
        menu2.setFont(font)
        menu3.setFont(font)
        menu4.setFont(font)
        menu5.setFont(font)


        addAction1 = QAction("View Population", self)
        addAction2 = QAction("View Fertility Rate", self)
        addAction3 = QAction("View Life Expectancy", self)

        addAction4 = QAction("Population Graphs", self)
        addAction5 = QAction("View Fertility Rate Graphs", self)
        addAction6 = QAction("View Life Expectancy Graphs", self)

        addAction7 = QAction("View Countries", self)
        addAction8 = QAction("View Country Code", self)

        addAction9 = QAction("Population Comparison", self)
        addAction10 = QAction("Fertility Rate Comparison", self)
        addAction11 = QAction("Life Expectancy Comparison", self)

        addAction12 = QAction("Numeric Analysis", self)
        addAction13 = QAction("Graphical Analysis", self)
        addAction14 = QAction("More Details", self)
        addAction15 = QAction("World Population 2018", self)

        addAction1.setIcon(QIcon("view.png"))
        addAction2.setIcon(QIcon("view.png"))
        addAction3.setIcon(QIcon("view.png"))
        addAction4.setIcon(QIcon("view.png"))
        addAction5.setIcon(QIcon("view.png"))
        addAction6.setIcon(QIcon("view.png"))
        addAction7.setIcon(QIcon("view.png"))
        addAction8.setIcon(QIcon("view.png"))
        addAction9.setIcon(QIcon("choose.png"))
        addAction10.setIcon(QIcon("choose.png"))
        addAction11.setIcon(QIcon("choose.png"))
        addAction12.setIcon(QIcon("a1.png"))
        addAction13.setIcon(QIcon("a2.png"))
        addAction14.setIcon(QIcon("a3.png"))
        addAction15.setIcon(QIcon("t1.png"))

        addAction1.setShortcut("Ctrl+M")
        addAction2.setShortcut("Ctrl+N")
        addAction3.setShortcut("Ctrl+O")

        addAction4.setShortcut("Ctrl+P")
        addAction5.setShortcut("Ctrl+Q")
        addAction6.setShortcut("Ctrl+R")

        addAction7.setShortcut("Ctrl+X")
        addAction8.setShortcut("Ctrl+Y")

        addAction9.setShortcut("Ctrl+A")
        addAction10.setShortcut("Ctrl+B")
        addAction11.setShortcut("Ctrl+C")

        addAction12.setShortcut("Ctrl+J")
        addAction13.setShortcut("Ctrl+K")
        addAction14.setShortcut("Ctrl+L")
        addAction15.setShortcut("Ctrl+W")

        addAction1.triggered.connect(self.showPopulation)
        addAction2.triggered.connect(self.showFertility)
        addAction3.triggered.connect(self.showLifeexpectancy)

        addAction4.triggered.connect(self.viewPopulation)
        addAction5.triggered.connect(self.viewFertility)
        addAction6.triggered.connect(self.viewLifeexpectancy)

        addAction7.triggered.connect(self.country)
        addAction8.triggered.connect(self.countryCode)

        addAction9.triggered.connect(self.comparePopulation)
        addAction10.triggered.connect(self.compareFertility)
        addAction11.triggered.connect(self.compareLife)

        addAction12.triggered.connect(self.numeric)
        addAction13.triggered.connect(self.graphical)
        addAction14.triggered.connect(self.more)
        addAction15.triggered.connect(self.world)


        menu1.addAction(addAction1)
        menu1.addAction(addAction2)
        menu1.addAction(addAction3)

        menu2.addAction(addAction4)
        menu2.addAction(addAction5)
        menu2.addAction(addAction6)

        menu3.addAction(addAction9)
        menu3.addAction(addAction10)
        menu3.addAction(addAction11)

        menu4.addAction(addAction7)
        menu4.addAction(addAction8)

        menu5.addAction(addAction12)
        menu5.addAction(addAction13)
        menu5.addAction(addAction14)
        menu5.addAction(addAction15)

        self.setWindowIcon(QIcon("icon.png"))
        self.show()



    def showPopulation(self):
        try:
            obj = ChooseNum.ChooseNum1(self)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def showFertility(self):
        try:
            obj = ChooseNum.ChooseNum2(self)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def showLifeexpectancy(self):
        try:
            obj = ChooseNum.ChooseNum3(self)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def viewPopulation(self):
        try:
            self.obj = ChooseCase.ChooseCase1(self)
            self.mdi.addSubWindow(self.obj)
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def viewFertility(self):
        try:
            self.obj = ChooseCase.ChooseCase2(self)
            self.mdi.addSubWindow(self.obj)
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def viewLifeexpectancy(self):
        try:
            self.obj = ChooseCase.ChooseCase3(self)
            self.mdi.addSubWindow(self.obj)
            self.obj.show()
        except BaseException as ex:
            print(ex)

    def comparePopulation(self):
        try :
            obj = CompareScreen.General1(self)
            self.mdi.addSubWindow(obj)
            obj.show()

        except BaseException as ex :
            print(ex)


    def compareLife(self):
        try :
            obj = CompareScreen.General3(self)
            self.mdi.addSubWindow(obj)
            obj.show()

        except BaseException as ex :
            print(ex)


    def compareFertility(self):
        try :
            obj = CompareScreen.General2(self)
            self.mdi.addSubWindow(obj)
            obj.show()

        except BaseException as ex :
            print(ex)



    def country(self):
        try :
            ob = Countries.CountriesScreen(self)
            self.mdi.addSubWindow(ob)
            ob.show()

        except BaseException as ex :
            print(ex)


    def countryCode(self):
        try :
            obj = Countries.CountriesCodeScreen(self)
            self.mdi.addSubWindow(obj)
            obj.show()

        except BaseException as ex :
            print(ex)

    def numeric(self):
        try:
            obj = LiveScreen.LiveScreen(self)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def graphical(self):
        try:
            obj = LiveScreen.LiveScreen2(self)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def more(self):
        try:
            obj = LiveScreen.LiveScreen3(self)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def world(self):
        try:
            obj = LiveScreen.World(self)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScreen()
    sys.exit(app.exec_())
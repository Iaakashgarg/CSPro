from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import random

data = pd.read_csv("country_population.csv")

class CountriesScreen(QDialog):
    def __init__(self,parent=None):
        super(CountriesScreen, self).__init__()
        self.parent=parent
        self.setWindowTitle(" Countries Table!!! ")
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        column_headers = ("Sr. No.", "Country Name", "Country Code")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.prepareTableData()
        grid.addWidget(self.tableWidget)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        afont = QFont()
        afont.setFamily("Comic Sans MS")
        afont.setPointSize(13)
        header.setFont(afont)
        self.setLayout(grid)
        self.show()

    def prepareTableData(self):
        try:
            row = 0
            c = data["Country Name"].count()
            record = data.iloc[0:264, 0:2]
            self.tableWidget.setRowCount(265)
            num = 1
            while(row < c) :
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(num)))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(record.iloc[row]["Country Name"]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(record.iloc[row]["Country Code"]))
                row += 1
                num = num+1

        except BaseException as ex:
            print(ex)


class CountriesCodeScreen(QDialog):
    def __init__(self,parent=None):
        super(CountriesCodeScreen, self).__init__()
        self.parent=parent
        self.setWindowTitle(" Know Your Country Code!!! ")
        grid = QGridLayout()
        self.setGeometry(230, 100, 800, 450)
        newfont = QFont("Comic Sans MS", 20, QFont.Bold )

        data = pd.read_csv("country_population.csv")

        label1 = QLabel("Choose Any Country : ")
        label1.setFont(newfont)
        btn1 = QPushButton("Show Country Code")
        btn1.setFont(newfont)
        self.combo1 = QComboBox()
        countries = data["Country Name"]
        self.combo1.addItems(countries)
        self.combo1.setFont(newfont)
        btn1.clicked.connect(self.action)
        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.combo1, 0, 1, 1, 2)
        grid.addWidget(btn1, 4, 0, 1, 4)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(800, 450)

        self.show()
        self.setLayout(grid)
        self.show()

    def action(self):
        try:
            country = self.combo1.currentText()
            ob = perform1(country,self.parent)
            self.parent.mdi.addSubWindow(ob)
            ob.show()
        except BaseException as ex:
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

class perform1(QDialog ):
    def __init__(self,country,parent=None):
        self.country = country
        self.parent = parent
        super(perform1, self).__init__()
        self.setWindowTitle(" Country Code Section!!! ")
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()
        newfont = QFont("Arial", 24, QFont.Bold)

        label1 = QLabel(self.country + "'s Country Code Is ")
        label1.move(50, 50)
        label1.setFont(newfont)

        code = (data[data["Country Name"] == self.country]["Country Code"]).item()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(str(code))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setFont(newfont)

        grid.addWidget(label1)
        grid.addWidget(msg)
        self.setLayout(grid)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CountriesCodeScreen()
    sys.exit(app.exec_())
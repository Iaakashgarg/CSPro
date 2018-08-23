from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MainScreen
import time


class Form(QDialog):
    """ Just a simple dialog with a couple of widgets
    """

    def __init__(self):
        super(Form, self).__init__()
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.lineedit = QLineEdit("Write something and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.update_ui)

    def update_ui(self):
        self.browser.append(self.lineedit.text())


    def keyPressEvent(self, QKeyEvent):
        #returnPressed = pyqtSignal
        try:
            self.obj = MainScreen.MainScreen()
            self.obj.show()
        except BaseException as ex:
            print(ex)

if __name__ == "__main__":
    import sys, time

    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('wert.jpg')
    splash_pix2 = splash_pix.scaled(QSize(800,500))
    splash = QSplashScreen(splash_pix2, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    # splash = QSplashScreen(splash_pix)
    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(8)
    progressBar.paintEngine()
    progressBar.setGeometry(0, splash_pix2.height() - 50, splash_pix2.width(), 20)

    # splash.setMask(splash_pix.mask())

    splash.show()
    splash.showMessage("<h1><font color='red'><font face='Comic Sans MS'>Welcome To CSPro!</font></h1>", Qt.AlignTop | Qt.AlignRight, Qt.black)

    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    form = Form()
    form.show()
    splash.finish(form)
    sys.exit(app.exec_())
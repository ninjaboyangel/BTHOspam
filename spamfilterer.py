# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('C:/Users/Noah/Documents/BTHOspam/test.ui', self)


        self.button = self.findChild(QtWidgets.QPushButton, 'testButton')
        self.button.clicked.connect(self.testButtonPressed)

        self.show()

    def testButtonPressed(self):
        print('testButtonPressed')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

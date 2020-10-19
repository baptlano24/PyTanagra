from PyQt5.uic.properties import QtCore

from Front.Welcome import Ui_MainWindow
from Front.Data_WIndow import Ui_Dialog
import sys
from PyQt5 import QtWidgets


def data_open():
    dia = Dia_Window()
    dia.exec_()


class Dia_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dia_Window, self).__init__(*args, **kwargs)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(data_open)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
print("Bienvenu PyTanagra")

import multiprocessing

from Front.Welcome import Ui_MainWindow
from Front.DiaWindow import Dia_Window
import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.data_open)
        self.dia = Dia_Window()
        self.result = None
        self.dia.trigger_result.connect(lambda x: self.result_launch(x))

    def data_open(self):
        """execute Dia_Window"""

        self.dia.clean()
        self.dia.exec_()

    def result_launch(self, list_res):
        self.result = None
        self.result = list_res
        for x in self.result:
            x.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    multiprocessing.freeze_support()
    window.show()
    app.exec()

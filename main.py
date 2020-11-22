import multiprocessing
import sklearn.model_selection
from PyQt5.QtWidgets import QMessageBox

from Front.Welcome import Ui_MainWindow
from Front.DiaWindow import Dia_Window
import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Window of PyTanagra :
    - Dia_Window()
    - list of Result Window """
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
        QMessageBox.information(self, "Attention", "Please note, PyTanagra only accepts csv files, please fill in only "
                                                   "Sep, na value, encoding and header. Otherwise PyTanagra will take "
                                                   "the default settings")
        self.dia.exec_()

    def result_launch(self, list_res):
        """Show all Result Window of the list"""
        self.result = None
        self.result = list_res
        for x in self.result:
            x.show()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

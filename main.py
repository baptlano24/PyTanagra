from PyQt5.QtWidgets import QFileDialog
from Front.Welcome import Ui_MainWindow
from Front.Data_WIndow import Ui_Dialog
import sys
from PyQt5 import QtWidgets


def data_open():
    dia = Dia_Window()
    dia.exec_()


class Dia_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(Dia_Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.browseButton.clicked.connect(self.browse_1)

    def browse_1(self):
        file = QFileDialog()
        filter_name = "Csv files (*.csv);;Text files (*.txt);;Xls files (*.xls);; Xlsx files (*.xlsx)"
        file.setNameFilter(filter_name)
        if file.exec():
            filenames = file.selectedFiles()
            self.browseLine.setText(str(filenames[0]))

            



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

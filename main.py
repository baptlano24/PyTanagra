from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Front.Welcome import Ui_MainWindow
from Front.Data_WIndow import Ui_Dialog
import pandas as pd
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
        self.buttonBox.accepted.connect(self.accept_value)

    def browse_1(self):
        file = QFileDialog()
        filter_name = "Csv files (*.csv);;Text files (*.txt);;Xls files (*.xls);; Xlsx files (*.xlsx)"
        file.setNameFilter(filter_name)
        if file.exec():
            filenames = file.selectedFiles()
            self.browseLine.setText(str(filenames[0]))

    def accept_value(self):
        if not (self.browseLine.text()):
            msgBox = QMessageBox.critical(self, "Erreur", "Pas de fichier à ouvrir")
            return
        file = self.browseLine.text()
        if not (self.lineEdit_sep.text()):
            sep = ','
        else:
            sep = self.lineEdit_sep.text()
        if not (self.lineEdit_na.text()):
            na_value = "‘’, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’, ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, " \
                       "‘<NA>’, ‘N/A’, ‘NA’, ‘NULL’," \
                       " ‘NaN’, ‘n/a’, " \
                       "‘nan’, ‘null’"
        else:
            na_value = self.lineEdit_na.text()
        if not (self.lineEdit_encod.text()):
            enc = None
        else:
            enc = self.lineEdit_encod.text()
        if not (self.lineEdit_head.text()):
            head = "infer"
        else:
            head = self.lineEdit_head.text()
        try:
            data = pd.read_csv(file, sep=sep, header=head, na_values=na_value, encoding=enc)
            print(data)

        except:
            QMessageBox.critical(self, "Erreur", "Erreur")


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

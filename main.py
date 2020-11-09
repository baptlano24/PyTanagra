import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QStringListModel
from Back.ML_data import ML_data
from Back.SVR import SVR_b
from Back.reg_lin import regression_lin
from Front.Welcome import Ui_MainWindow
from Front.Data_WIndow import Ui_Dialog
from Front.SelectVar import SelectVar
from Front.ModelQuant import ModelQua
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
        self.ml_data = ML_data()
        self.select_var = SelectVar()
        self.select_var.trigger.connect(lambda x: self.test(x))
        self.model_qua = ModelQua()
        self.model_qua.trigger_model.connect(lambda x: self.model_qua_launch(x))

    def test(self, test):
        print(test[1])
        self.ml_data.set_target(test[0])
        self.ml_data.set_features(test[1])
        print(str(self.ml_data.target_type))
        if self.ml_data.target_type.all() == np.float64 or self.ml_data.target_type.all() == np.int64:
            print("Quantitative")
            self.model_qua.open()
        else:
            print("QUALI")
            self.model_qua.open()

    def model_qua_launch(self,dict):
        if "SVR" in dict:
            SVR = dict["SVR"]
            if SVR["Auto"]:
                result = SVR_b(self.ml_data.feature,self.ml_data.target,SVR["Auto"])
                print("SVR",result)
            else:
                print(self.ml_data.feature)
                print(self.ml_data.target)
                result = SVR_b(self.ml_data.feature, self.ml_data.target, SVR["Auto"], [SVR["C"], SVR["Kernel"],SVR["Degree"]])
                print("SVR",result)
        elif "LR" in dict:
            LR = dict["LR"]
            if LR["Auto"]:
                result = regression_lin(self.ml_data.feature,self.ml_data.target, LR["Auto"])
                print("LR",result)
            else:
                result = regression_lin(self.ml_data.feature,self.ml_data.target, LR["Auto"], LR["test_size"])
                print("LR",result)



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
            self.ml_data.set_pd_data(data)
            A = QStringListModel(data.columns.tolist())
            self.select_var.Variables.setModel(A)
        except:

            QMessageBox.critical(self, "Erreur", "Erreur")
        self.select_var.exec_()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(data_open)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
print("Bienvenue PyTanagra")

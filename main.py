import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QStringListModel
from Back.ML_data import ML_data
from Back.SVR import SVR_b
from Back.reg_lin import regression_lin
from Back.TreeReg import RegTree
from Front.Welcome import Ui_MainWindow
from Front.Data_WIndow import Ui_Dialog
from Front.SelectVar import SelectVar
from Front.ModelQuant import ModelQua
import pandas as pd
import sys
from PyQt5 import QtWidgets


def data_open():
    """execute Dia_Window"""
    dia = Dia_Window()
    dia.exec_()


class Dia_Window(QtWidgets.QDialog, Ui_Dialog):
    """Dialogue Window which have :
     - Download data
     - ML Data
     - SelectVar()
     - ModelQua()"""
    def __init__(self, *args, **kwargs):
        super(Dia_Window, self).__init__(*args, **kwargs)
        # Initializing from ui.file (designer)
        self.setupUi(self)
        # When "browe" is clicked
        self.browseButton.clicked.connect(self.browse_1)
        # When "Ok" is clicked
        self.buttonBox.accepted.connect(self.accept_value)
        self.ml_data = ML_data()
        self.select_var = SelectVar()
        # When the signal of SelectVar() is "emitted"
        self.select_var.trigger.connect(lambda x: self.test(x))
        self.model_qua = ModelQua()
        # When the signal of ModelQua() is "emitted"
        self.model_qua.trigger_model.connect(lambda x: self.model_qua_launch(x))

    def test(self, test):
        """setting of Target and Features of ML_data + choose beetween ModelQua() or ModelQuali()
         depend of Target type"""
        self.ml_data.set_target(test[0])
        self.ml_data.set_features(test[1])
        if self.ml_data.target_type.all() == np.float64 or self.ml_data.target_type.all() == np.int64:
            print("Quantitative")
            self.model_qua.open()
        else:
            print("QUALI")

    def model_qua_launch(self, dict):
        """Launch all model Quantitative from dict signal of ModelQua()"""
        if "SVR" in dict:
            SVR = dict["SVR"]
            if SVR["Auto"]:
                result = SVR_b(self.ml_data.feature, self.ml_data.target, SVR["Auto"])
                print("SVR", result)
            else:
                print(self.ml_data.feature)
                print(self.ml_data.target)
                result = SVR_b(self.ml_data.feature, self.ml_data.target, SVR["Auto"], [SVR["C"],
                                                                                        SVR["Kernel"],
                                                                                        SVR["Degree"]])
                print("SVR", result)
        if "LR" in dict:
            LR = dict["LR"]
            if LR["Auto"]:
                result = regression_lin(self.ml_data.feature, self.ml_data.target, LR["Auto"])
                print("LR", result)
            else:
                result = regression_lin(self.ml_data.feature, self.ml_data.target, LR["Auto"], LR["test_size"])
                print("LR", result)
        if "RT" in dict:
            RT = dict["RT"]
            if RT["Auto"]:
                result = RegTree(self.ml_data.feature, self.ml_data.target, RT["Auto"])
                print("RT", result)
            else:
                result = RegTree(self.ml_data.feature, self.ml_data.target, RT["Auto"], [RT["Criterion"],
                                                                                         RT["Min_Samples_Split"],
                                                                                         RT["Min_Samples_Leaf"]])
                print("RT", result)

    def browse_1(self):
        """Function which browse csv file/Text file/Xlsx file"""
        file = QFileDialog()
        filter_name = "Csv files (*.csv);;Text files (*.txt);;Xls files (*.xls);; Xlsx files (*.xlsx)"
        file.setNameFilter(filter_name)
        if file.exec():
            filenames = file.selectedFiles()
            self.browseLine.setText(str(filenames[0]))

    def accept_value(self):
        """Function who take all information from the windows and applicate read_csv and more
        if we have time"""
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

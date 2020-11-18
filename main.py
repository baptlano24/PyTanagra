import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QStringListModel, pyqtSignal
from Front.ResultQuant import Window_Quant
from Back.ML_data import ML_data
from Back.SVR import SVR_b
from Back.reg_lin import regression_lin
from Back.TreeReg import RegTree
from Back.KNN import knn_class
from Back.arbre_classif import arbre_clas
from Back.LogReg import LogReg
from Front.Welcome import Ui_MainWindow
from Front.Data_WIndow import Ui_Dialog
from Front.SelectVar import SelectVar
from Front.ModelQuant import ModelQua
from Front.ModelQuali import ModelQualitative
from Front.ResultQuali import Window
import pandas as pd
import seaborn as sn
import sys
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets


class Dia_Window(QtWidgets.QDialog, Ui_Dialog):
    trigger_result = pyqtSignal(list)

    """- Download data
     - ML Data
     - SelectVar()
     - ModelQua()"""

    def __init__(self, *args, **kwargs):
        super(Dia_Window, self).__init__(*args, **kwargs)
        # Initializing from ui.file (designer)
        self.setupUi(self)
        # When "browse" is clicked
        self.browseButton.clicked.connect(self.browse_1)
        # When "Ok" is clicked
        self.buttonBox.accepted.connect(self.accept_value)
        self.ml_data = ML_data()
        self.select_var = SelectVar()
        # When the signal of SelectVar() is "emitted"
        self.select_var.trigger.connect(lambda x: self.test(x))
        self.model_qua = ModelQua()
        self.model_quali = ModelQualitative()
        self.result_quali = Window()
        # When the signal of ModelQua() is "emitted"
        self.model_qua.trigger_model.connect(lambda x: self.model_qua_launch(x))
        self.model_quali.trigger_model.connect(lambda x: self.model_qua_launch(x))

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
            self.model_quali.open()

    def model_qua_launch(self, dict):
        """Launch all model Quantitative from dict signal of ModelQua()"""
        list_result = []
        if "SVR" in dict:
            SVR = dict["SVR"]
            if SVR["Auto"]:
                result = SVR_b(self.ml_data.feature, self.ml_data.target, SVR["Auto"])
                print("SVR", result)
                model, score, graph, time = result
                result_win = Window_Quant()
                result_win.setWindowTitle("SVT Result Auto")
                result_win.setData(model, score, graph, time)
                list_result.append(result_win)
            else:
                print(self.ml_data.feature)
                print(self.ml_data.target)
                result = SVR_b(self.ml_data.feature, self.ml_data.target, SVR["Auto"], [SVR["C"],
                                                                                        SVR["Kernel"],
                                                                                        SVR["Degree"]])
                model, score, graph, time = result
                result_win = Window_Quant()
                result_win.setWindowTitle("SVT Result")
                result_win.setData(model, score, graph, time)
                list_result.append(result_win)
                print("SVR", result)
        if "LR" in dict:
            LR = dict["LR"]
            if LR["Auto"]:
                result = regression_lin(self.ml_data.feature, self.ml_data.target, LR["Auto"])
                print("LR", result)
                model, score, graph, time = result
                result_win = Window_Quant()
                result_win.setWindowTitle("Linear Regression Result Auto")
                result_win.setData(model, score, graph, time)
                list_result.append(result_win)
            else:
                result = regression_lin(self.ml_data.feature, self.ml_data.target, LR["Auto"], LR["fit_intercept"], LR["normalize"])
                model, score, graph, time = result
                result_win = Window_Quant()
                result_win.setWindowTitle("Linear Regression Result")
                result_win.setData(model, score, graph, time)
                list_result.append(result_win)
                print("LR", result)
        if "RT" in dict:
            RT = dict["RT"]
            if RT["Auto"]:
                result = RegTree(self.ml_data.feature, self.ml_data.target, RT["Auto"])
                model, score, graph, time = result
                result_win = Window_Quant()
                result_win.setWindowTitle("Regression Tree Result Auto")
                result_win.setData(model, score, graph, time)
                list_result.append(result_win)
                print("RT", result)
            else:
                result = RegTree(self.ml_data.feature, self.ml_data.target, RT["Auto"], [RT["Criterion"],
                                                                                         RT["Min_Samples_Split"],
                                                                                         RT["Min_Samples_Leaf"]])
                model, score, graph, time = result
                result_win = Window_Quant()
                result_win.setWindowTitle("Regression Tree Result")
                result_win.setData(model, score, graph, time)
                list_result.append(result_win)
                print("RT", result)

        if "KNN" in dict:
            KNN = dict["KNN"]
            print(KNN)
            if KNN["Auto"]:
                result = knn_class(self.ml_data.feature, self.ml_data.target, KNN["Auto"])
                model, matrix, dict_cr, graph, time = result
                print("KNN", result)
                result_win = Window()
                result_win.setWindowTitle("KNN Result Auto")
                result_win.setData(model, matrix, dict_cr, graph, time)
                list_result.append(result_win)
            else:
                result = knn_class(self.ml_data.feature, self.ml_data.target, KNN["Auto"],
                                   [KNN["leaf_size"], KNN["n_neighbors"], KNN["p"], KNN["metric"]])
                print("KNN", result)
                model, matrix, dict_cr, graph, time = result
                # sn.set(font_scale=1.4)  # for label size
                # sn.heatmap(result[1], annot=True, annot_kws={"size": 16})  # font size
                # plt.show()
                self.model_quali.close()
                # self.result_quali.widget.set_data(result[1])
                result_win = Window()
                result_win.setWindowTitle("KNN Result")
                result_win.setData(model, matrix, dict_cr, graph, time)
                list_result.append(result_win)
        if "LogiR" in dict:
            LogiR = dict["LogiR"]
            if LogiR["Auto"]:
                result = LogReg(self.ml_data.feature, self.ml_data.target, LogiR["Auto"])
                print("LogiR", result)
                model, matrix, dict_cr, graph, time = result
                result_win = Window()
                result_win.setWindowTitle("Logistic Regression Result Auto")
                result_win.setData(model, matrix, dict_cr, graph, time)
                list_result.append(result_win)
            else:
                result = LogReg(self.ml_data.feature, self.ml_data.target, LogiR["Auto"], [LogiR['C'],
                                                                                           LogiR['penalty']])
                model, matrix, dict_cr, graph, time = result
                result_win = Window()
                result_win.setWindowTitle("Logistic Regression Result")
                result_win.setData(model, matrix, dict_cr, graph, time)
                list_result.append(result_win)
                print("LogiR", result)
        if "DTC" in dict:
            DTC = dict["DTC"]
            if DTC["Auto"]:
                result = arbre_clas(self.ml_data.feature, self.ml_data.target, DTC["Auto"])
                print("result ?")
                model, matrix, dict_cr, graph, time = result
                result_win = Window()
                result_win.setWindowTitle("Tree Decision Classification Auto")
                result_win.setData(model, matrix, dict_cr, graph, time)
                list_result.append(result_win)

            else:
                result = arbre_clas(self.ml_data.feature, self.ml_data.target, DTC["Auto"],DTC["max_leaf_nodes"],DTC["max_depth"],DTC["min_samples_split"])
                model, matrix, dict_cr, graph, time = result
                print("result no Auto ?")
                result_win = Window()
                result_win.setWindowTitle("Tree Decision Classification")
                result_win.setData(model, matrix, dict_cr, graph, time)
                list_result.append(result_win)


        self.close()
        self.trigger_result.emit(list_result)

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
        self.pushButton.clicked.connect(self.data_open)
        self.dia = Dia_Window()
        self.result = None
        self.dia.trigger_result.connect(lambda x: self.result_launch(x))

    def data_open(self):
        """execute Dia_Window"""
        self.dia.exec_()

    def result_launch(self, list_res):
        self.result = list_res
        for x in self.result:
            x.show()
        del self.dia
        self.dia = Dia_Window()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
print("Bienvenue PyTanagra")

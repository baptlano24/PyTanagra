from PyQt5.QtCore import pyqtSignal

from Front.ui_model_quant import Ui_Model_quanti
from PyQt5 import QtWidgets


class ModelQua(QtWidgets.QDialog, Ui_Model_quanti):
    trigger_model = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super(ModelQua, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.SVR_c.setReadOnly(True)
        self.SVR_auto.setDisabled(True)
        self.SVR_degree.setReadOnly(True)
        self.combo_kernel.setDisabled(True)
        self.LR_auto.setDisabled(True)
        self.LR_size.setDisabled(True)
        self.SVR_use.toggled.connect(self.svr_use)
        self.LR_use.toggled.connect(self.lr_use)
        self.LR_auto.toggled.connect(self.lr_auto)

        self.SVR_auto.toggled.connect(self.svr_auto)
        self.buttonBox.accepted.connect(self.accept_model)

    def lr_use(self):
        if self.LR_use.isChecked():
            self.LR_auto.setDisabled(False)

    def svr_use(self):
        if self.SVR_use.isChecked():
            self.SVR_c.setReadOnly(False)
            self.SVR_auto.setDisabled(False)
            self.SVR_degree.setReadOnly(False)
            self.combo_kernel.setDisabled(False)
        else:
            self.SVR_c.setReadOnly(True)
            self.SVR_auto.setDisabled(True)
            self.SVR_degree.setReadOnly(True)
            self.combo_kernel.setDisabled(True)

    def svr_auto(self):
        if self.SVR_auto.isChecked():
            self.SVR_c.setReadOnly(True)
            self.SVR_degree.setReadOnly(True)
            self.combo_kernel.setDisabled(True)
        else:
            self.SVR_c.setReadOnly(False)
            self.SVR_degree.setReadOnly(False)
            self.combo_kernel.setDisabled(False)

    def lr_auto(self):
        if self.LR_auto.isChecked():
            self.LR_size.setDisabled(True)

    def accept_model(self):
        dict_model = {}
        if self.LR_use.isChecked():
            dict_model["LR"] = {}
            if self.LR_use.isChecked():
                dict_model["LR"]["Auto"] = True
            else:
                dict_model["LR"]["Auto"] = False
                dict_model["LR"]["test_size"] = int(self.LR_size.text())
        if self.SVR_use.isChecked():
            dict_model["SVR"] = {}
            if self.SVR_auto.isChecked():
                dict_model["SVR"]["Auto"] = True
            else:
                dict_model["SVR"]["Auto"] = False
                dict_model["SVR"]["Kernel"] = self.combo_kernel.currentText()
                dict_model["SVR"]["C"] = int(self.SVR_c.text())
                dict_model["SVR"]["Degree"] = int(self.SVR_degree.text())
        self.close()
        self.trigger_model.emit(dict_model)

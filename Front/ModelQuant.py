from PyQt5.QtCore import pyqtSignal

from Front.ui_model_quant import Ui_Model_quanti
from PyQt5 import QtWidgets


class ModelQua(QtWidgets.QDialog, Ui_Model_quanti):
    """ Menu which allows to select among 3 algorithms
    when the target is quantitative. User can choose auto mode or
    tune hyperparameters"""
    trigger_model = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super(ModelQua, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # SVR Widget,
        # Initiation where widgets are disabled
        self.SVR_c.setReadOnly(True)
        self.SVR_auto.setDisabled(True)
        self.SVR_degree.setReadOnly(True)
        self.combo_kernel.setDisabled(True)
        # LR Widget,
        # Initiation where widgets are disabled
        self.LR_auto.setDisabled(True)
        self.LR_size.setReadOnly(True)
        # RT Widget,
        # Initiation where widgets are disabled
        self.RT_auto.setDisabled(True)
        self.RT_mss.setReadOnly(True)
        self.RT_mse.setReadOnly(True)
        self.combo_criterion.setDisabled(True)
        # When CheckBox of RT is toggled
        self.RT_use.toggled.connect(self.rt_use)
        self.RT_auto.toggled.connect(self.rt_auto)
        # When CheckBox of SVR is toggled
        self.SVR_use.toggled.connect(self.svr_use)
        self.SVR_auto.toggled.connect(self.svr_auto)
        # When CheckBox of LR is toggled
        self.LR_use.toggled.connect(self.lr_use)
        self.LR_auto.toggled.connect(self.lr_auto)
        # When the Users clicked on the button "Ok"
        self.buttonBox.accepted.connect(self.accept_model)

    def rt_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
         Else still disabled adn we clear the line edits"""
        if self.RT_use.isChecked():
            self.RT_auto.setDisabled(False)
            self.RT_mse.setReadOnly(False)
            self.RT_mss.setReadOnly(False)
            self.combo_criterion.setDisabled(False)
        else:
            self.RT_mse.clear()
            self.RT_mss.clear()
            self.RT_auto.setDisabled(True)
            self.RT_mse.setReadOnly(True)
            self.RT_mss.setReadOnly(True)
            self.combo_criterion.setDisabled(True)

    def rt_auto(self):
        """When 'Auto' checkbox is checked => All Hyperparameter are disabled and clear
        Else still All Hyperparameter are allowed"""
        if self.RT_auto.isChecked():
            self.RT_mse.clear()
            self.RT_mss.clear()
            self.RT_mse.setReadOnly(True)
            self.RT_mss.setReadOnly(True)
            self.combo_criterion.setDisabled(True)

        else:
            self.RT_mse.setReadOnly(False)
            self.RT_mss.setReadOnly(False)
            self.combo_criterion.setDisabled(False)

    def lr_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
        Else still disabled adn we clear the line edits"""

        if self.LR_use.isChecked():
            self.LR_auto.setDisabled(False)
            self.LR_size.setReadOnly(False)
        else:
            self.LR_size.clear()
            self.LR_auto.setDisabled(True)
            self.LR_size.setDisabled(True)

    def svr_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
        Else still disabled adn we clear the line edits"""
        if self.SVR_use.isChecked():
            self.SVR_c.setReadOnly(False)
            self.SVR_auto.setDisabled(False)
            self.SVR_degree.setDisabled(False)
            self.combo_kernel.setDisabled(False)
        else:
            self.SVR_degree.clear()
            self.SVR_c.clear()
            self.SVR_c.setReadOnly(True)
            self.SVR_auto.setDisabled(True)
            self.SVR_degree.setReadOnly(True)
            self.combo_kernel.setDisabled(True)

    def svr_auto(self):
        """When 'Auto' checkbox is checked => All Hyperparameter are disabled and clear
        Else still All Hyperparameter are allowed"""
        if self.SVR_auto.isChecked():
            self.SVR_degree.clear()
            self.SVR_c.clear()
            self.SVR_c.setReadOnly(True)
            self.SVR_degree.setReadOnly(True)
            self.combo_kernel.setDisabled(True)
        else:
            self.SVR_c.setReadOnly(False)
            self.SVR_degree.setReadOnly(False)
            self.combo_kernel.setDisabled(False)

    def lr_auto(self):
        """When 'Auto' checkbox is checked => All Hyperparameter are disabled and clear
            Else still All Hyperparameter are allowed"""
        if self.LR_auto.isChecked():
            self.LR_size.clear()
            self.LR_size.setReadOnly(True)
        else:
            self.LR_size.setReadOnly(False)

    def accept_model(self):
        """When user click on Ok, all the informations
         All the info is collected and structured in dict (Ex: {SVR: {Auto: False,C: ...}} )
         and sent as a signal."""
        dict_model = {}
        if self.LR_use.isChecked():
            dict_model["LR"] = {}
            if self.LR_auto.isChecked():
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
        if self.RT_use.isChecked():
            dict_model["RT"] = {}
            if self.RT_auto.isChecked():
                dict_model["RT"]["Auto"] = True
            else:
                dict_model["RT"]["Auto"] = False
                dict_model["RT"]["Criterion"] = self.combo_criterion.currentText()
                dict_model["RT"]["Min_Samples_Split"] = int(self.RT_mss.text())
                dict_model["RT"]["Min_Samples_Leaf"] = int(self.RT_mse.text())
        self.close()
        self.trigger_model.emit(dict_model)

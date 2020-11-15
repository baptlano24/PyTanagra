from PyQt5.QtCore import pyqtSignal

from Front.ui_model_quali import Ui_Model_quali
from PyQt5 import QtWidgets


class ModelQualitative(QtWidgets.QDialog, Ui_Model_quali):
    """ Menu which allows to select among 3 algorithms
    when the target is quantitative. User can choose auto mode or
    tune hyperparameters"""
    trigger_model = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super(ModelQualitative, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # LogiR Widget,
        # Initiation where widgets are disabled
        self.LogiR_C.setReadOnly(True)
        self.LogiR_auto.setDisabled(True)
        self.combo_penality.setDisabled(True)
        # Tree Widget,
        # Initiation where widgets are disabled
        # KNN Widget,
        # Initiation where widgets are disabled
        self.KNN_auto.setDisabled(True)
        self.KNN_n.setReadOnly(True)
        self.KNN_leafsize.setReadOnly(True)
        self.combo_metric.setDisabled(True)
        self.combo_p.setDisabled(True)
        # When CheckBox of LogiR_C is toggled
        self.LogiR_use.toggled.connect(self.log_use)
        self.LogiR_auto.toggled.connect(self.log_auto)
        # When CheckBox of KNN  is toggled
        self.KNN_use.toggled.connect(self.knn_use)
        self.KNN_auto.toggled.connect(self.knn_auto)
        # When CheckBox of LR is toggled
        #self.LR_use.toggled.connect(self.lr_use)
        #self.LR_auto.toggled.connect(self.lr_auto)
        # When the Users clicked on the button "Ok"
        self.buttonBox.accepted.connect(self.accept_model)

    def log_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
         Else still disabled adn we clear the line edits"""

        if self.LogiR_use.isChecked():
            self.LogiR_auto.setDisabled(False)
            self.LogiR_C.setReadOnly(False)
            self.combo_penality.setDisabled(False)
        else:
            self.LogiR_C.clear()
            self.LogiR_auto.setDisabled(True)
            self.LogiR_C.setReadOnly(True)
            self.combo_penality.setDisabled(True)

    def log_auto(self):
        """When 'Auto' checkbox is checked => All Hyperparameter are disabled and clear
             Else still All Hyperparameter are allowed"""

        if self.LogiR_auto.isChecked():
            self.LogiR_C.clear()
            self.LogiR_C.setReadOnly(True)
            self.combo_penality.setDisabled(True)
        else:
            self.LogiR_C.setReadOnly(False)
            self.combo_penality.setDisabled(False)

    def knn_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
         Else still disabled adn we clear the line edits"""

        if self.KNN_use.isChecked():
            self.KNN_auto.setDisabled(False)
            self.KNN_n.setReadOnly(False)
            self.KNN_leafsize.setReadOnly(False)
            self.combo_p.setDisabled(False)
            self.combo_metric.setDisabled(False)
        else:
            self.KNN_n.clear()
            self.KNN_leafsize.clear()
            self.KNN_n.setReadOnly(True)
            self.KNN_leafsize.setReadOnly(True)
            self.combo_p.setDisabled(True)
            self.combo_metric.setDisabled(True)

    def knn_auto(self):
        """When 'Auto' checkbox is checked => All Hyperparameter are disabled and clear
        Else still All Hyperparameter are allowed"""

        if self.KNN_auto.isChecked():
            self.KNN_n.clear()
            self.KNN_leafsize.clear()
            self.KNN_n.setReadOnly(True)
            self.KNN_leafsize.setReadOnly(True)
            self.combo_p.setDisabled(True)
            self.combo_metric.setDisabled(True)

        else:
            self.KNN_n.setReadOnly(False)
            self.KNN_leafsize.setReadOnly(False)
            self.combo_p.setDisabled(False)
            self.combo_metric.setDisabled(False)

    def accept_model(self):
        """When user click on Ok, all the informations
         All the info is collected and structured in dict (Ex: {SVR: {Auto: False,C: ...}} )
         and sent as a signal."""
        dict_model = {}
        if self.KNN_use.isChecked():
            dict_model["KNN"] = {}
            if self.KNN_auto.isChecked():
                dict_model["KNN"]["Auto"] = True
            else:
                dict_model["KNN"]["Auto"] = False
                dict_model["KNN"]["leaf_size"] = int(self.KNN_leafsize.text())
                dict_model["KNN"]["n_neighbors"] = int(self.KNN_n.text())
                dict_model["KNN"]["p"] = self.combo_p.currentText()
                dict_model["KNN"]["metric"] = self.combo_metric.currentText()
        if self.LogiR_use.isChecked():
            dict_model["LogiR"] = {}
            if self.LogiR_auto.isChecked():
                dict_model["LogiR"]["Auto"] = True
            else:
                dict_model["LogiR"]["Auto"] = False
                dict_model["LogiR"]["C"] = int(self.LogiR_C.text())
                dict_model["LogiR"]["penalty"] = self.combo_penality.currentText()

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


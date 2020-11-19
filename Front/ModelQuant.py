from PyQt5.QtCore import pyqtSignal

from Front.ui_model_quant import Ui_Model_quanti
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox


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
        self.combo_intercept.setDisabled(True)
        self.combo_norm.setDisabled(True)

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
            self.combo_intercept.setDisabled(False)
            self.combo_norm.setDisabled(False)
        else:
            self.combo_intercept.setDisabled(True)
            self.combo_norm.setDisabled(True)
            self.LR_auto.setDisabled(True)

    def svr_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
        Else still disabled adn we clear the line edits"""
        if self.SVR_use.isChecked():
            self.SVR_c.setReadOnly(False)
            self.SVR_auto.setDisabled(False)
            self.SVR_degree.setReadOnly(False)
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
            self.combo_intercept.setDisabled(True)
            self.combo_norm.setDisabled(True)
        else:
            self.combo_intercept.setDisabled(False)
            self.combo_norm.setDisabled(False)

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
                dict_model["LR"]["fit_intercept"] = (self.combo_intercept.currentText() == "True")
                dict_model["LR"]["normalize"] = (self.combo_intercept.currentText() == "True")

        if self.SVR_use.isChecked():
            dict_model["SVR"] = {}
            if self.SVR_auto.isChecked():
                dict_model["SVR"]["Auto"] = True
            else:
                dict_model["SVR"]["Auto"] = False
                dict_model["SVR"]["Kernel"] = self.combo_kernel.currentText()

                # Verification of the parameter C
                if self.SVR_c.text() == '':
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "C est vide.\nC correspond à la pénalisation L2 du modèle. C doit être un réel positif. Si vous souhaitez un modèle non pénalisé, il suffit d'avoir C=0.")
                elif float(self.SVR_c.text()) >= 0:
                    dict_model["SVR"]["C"] = float(self.SVR_c.text())
                else:
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "C correspond à la pénalisation L2 du modèle. C doit être un réel positif. Si vous souhaitez un modèle non pénalisé, il suffit d'avoir C=0.")

                if self.combo_kernel.currentText() == 'poly':
                    dict_model["SVR"]["Degree"] = int(self.SVR_degree.text())
                else:
                    dict_model["SVR"]["Degree"] = None
        if self.RT_use.isChecked():
            dict_model["RT"] = {}
            if self.RT_auto.isChecked():
                dict_model["RT"]["Auto"] = True
            else:
                dict_model["RT"]["Auto"] = False
                dict_model["RT"]["Criterion"] = self.combo_criterion.currentText()

                # Verification of the parameter Min_Samples_Split
                if self.RT_mss.text() == '':
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "Min_Samples_Split est vide.\nMin_Samples_Split est soit un entier supérieur à 2 et dans ce cas, il correspond au nombre minumum nécessaire à la création d'un nœud. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer un nœud.")
                elif int(float(self.RT_mss.text())) == float(self.RT_mss.text()) and int(
                        float(self.RT_mss.text())) >= 2:
                    dict_model["RT"]["Min_Samples_Split"] = int(self.RT_mss.text())
                elif float(self.RT_mss.text()) <= 1 and float(self.RT_mss.text()) > 0:
                    dict_model["RT"]["Min_Samples_Split"] = float(self.RT_mss.text())
                else:
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "Min_Samples_Split est soit un entier supérieur à 2 et dans ce cas, il correspond au nombre minumum nécessaire à la création d'un nœud. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer un nœud.")

                # Verification of the parameter Min_Samples_Leaf
                if self.RT_mse.text() == '':
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "Min_Samples_Leaf est vide.\nMin_Samples_Leaf est soit un entier supérieur à 1 et dans ce cas, il correspond au nombre minumum nécessaire à la création d'une feuille. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer une feuille.")
                if int(float(self.RT_mse.text())) == float(self.RT_mse.text()) and int(float(self.RT_mse.text())) >= 1:
                    dict_model["RT"]["Min_Samples_Leaf"] = int(self.RT_mse.text())
                elif float(self.RT_mse.text()) <= 1 and float(self.RT_mse.text()) > 0:
                    dict_model["RT"]["Min_Samples_Leaf"] = float(self.RT_mse.text())
                else:
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "Min_Samples_Leaf est soit un entier supérieur à 1 et dans ce cas, il correspond au nombre minumum nécessaire à la création d'une feuille. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer une feuille.")
        self.close()
        self.trigger_model.emit(dict_model)

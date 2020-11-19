from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

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
        self.LogiR_use.toggled.connect(self.log_use)
        self.LogiR_auto.toggled.connect(self.log_auto)
        # Tree Widget,
        # Initiation where widgets are disabled
        # KNN Widget,
        # Initiation where widgets are disabled
        self.KNN_auto.setDisabled(True)
        self.KNN_n.setReadOnly(True)
        self.KNN_leafsize.setReadOnly(True)
        self.combo_metric.setDisabled(True)
        self.combo_p.setDisabled(True)
        # Tree Widget,
        # Initiation where widgets are disabled
        self.DTC_mss.setReadOnly(True)
        self.DTC_maxd.setReadOnly(True)
        self.DTC_maxleafN.setReadOnly(True)
        # When CheckBox of DTC is toggled
        self.DTC_use.toggled.connect(self.dtc_use)
        self.DTC_auto.toggled.connect(self.dtc_auto)
        # When CheckBox of KNN  is toggled
        self.KNN_use.toggled.connect(self.knn_use)
        self.KNN_auto.toggled.connect(self.knn_auto)
        # When the Users clicked on the button "Ok"
        self.buttonBox.accepted.connect(self.accept_model)

    def dtc_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
        Else still disabled adn we clear the line edits"""
        if self.DTC_use.isChecked():
            self.DTC_auto.setDisabled(False)
            self.DTC_mss.setReadOnly(False)
            self.DTC_maxd.setReadOnly(False)
            self.DTC_maxleafN.setReadOnly(False)
        else:
            self.DTC_mss.setReadOnly(True)
            self.DTC_maxd.setReadOnly(True)
            self.DTC_maxleafN.setReadOnly(True)
            self.DTC_maxleafN.clear()
            self.DTC_maxd.clear()
            self.DTC_mss.clear()
            self.DTC_auto.setDisabled(True)

    def dtc_auto(self):
        """When 'Auto' checkbox is checked => All Hyperparameter are disabled and clear
             Else still All Hyperparameter are allowed"""
        if self.DTC_auto.isChecked():
            self.DTC_mss.setReadOnly(True)
            self.DTC_maxd.setReadOnly(True)
            self.DTC_maxleafN.setReadOnly(True)
            self.DTC_maxleafN.clear()
            self.DTC_maxd.clear()
            self.DTC_mss.clear()
        else:
            self.DTC_mss.setReadOnly(False)
            self.DTC_maxd.setReadOnly(False)
            self.DTC_maxleafN.setReadOnly(False)


    def log_use(self):
        """When 'Use ? checkbox is checked => All Hyperparameter and Auto Checkbox is allowed
         Else still disabled adn we clear the line edits"""
        if self.LogiR_use.isChecked():
            print("FDP REAGI")
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
            self.LogiR_C.clear()
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
                dict_model["KNN"]["p"] = self.combo_p.currentText()
                dict_model["KNN"]["metric"] = self.combo_metric.currentText()
                # Verification of the parameter leaf size
                if self.KNN_leafsize.text()=='':
                    QMessageBox.critical(self, "Erreur de paramètre","Leaf Size est vide. Leaf Size doit être un entier supérieur ou égal à 1.")
                elif float(self.KNN_leafsize.text())>=1 and int(float(self.KNN_leafsize.text()))==float(self.KNN_leafsize.text()):
                    dict_model["KNN"]["leaf_size"] = int(float(self.KNN_leafsize.text()))
                else:
                    QMessageBox.critical(self, "Erreur de paramètre", "Leaf Size doit être un entier supérieur ou égal à 1.")
                    return
                # Verification of the parameter n_neighbors
                if self.KNN_n.text()=='':
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "n_neighbors est vide. n_neighbors doit être un entier supérieur ou égal à 1.")
                elif float(self.KNN_n.text())>=1 and float(self.KNN_n.text())==int(float(self.KNN_n.text())):
                    dict_model["KNN"]["n_neighbors"] = int(float(self.KNN_n.text()))
                else:
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "n_neighbors doit être un entier supérieur ou égal à 1.")
                    return
        if self.LogiR_use.isChecked():
            dict_model["LogiR"] = {}
            if self.LogiR_auto.isChecked():
                dict_model["LogiR"]["Auto"] = True
            else:
                dict_model["LogiR"]["Auto"] = False
                dict_model["LogiR"]["penalty"] = self.combo_penality.currentText()
                # Verification of the parameter C
                if self.LogiR_C.text()=='':
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "C est vide.\nC correspond à la pénalisation du modèle choisi. C doit être un réel positif. Si vous souhaitez un modèle non pénalisé, il suffit d'avoir C=0 et de sélection n'importe quelle pénalité.")

                elif float(self.LogiR_C.text())>=0:
                    dict_model["LogiR"]["C"] = float(self.LogiR_C.text())
                else:
                    QMessageBox.critical(self, "Erreur de paramètre", "C correspond à la pénalisation du modèle choisi. C doit être un réel positif. Si vous souhaitez un modèle non pénalisé, il suffit d'avoir C=0 et de sélection n'importe quelle pénalité.")
                    return
        if self.DTC_use.isChecked():
            dict_model["DTC"] = {}
            if self.DTC_auto.isChecked():
                dict_model["DTC"]["Auto"] = True
            else:
                dict_model["DTC"]["Auto"] = False

                # Verification of the parameter Max Leaf Nodes
                if self.DTC_maxleafN.text()=='':
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "max_leaf_nodes est vide.\nmax_leaf_nodes correspond au nombre maximal de nœuds dans l'arbre. C'est un entier supérieur ou égal à 1 ou bien il prend la valeur None si vous ne souhaitez pas de limite.")
                elif self.DTC_maxleafN.text()=='None':
                    dict_model["DTC"]["max_leaf_nodes"]=None
                elif int(float(self.DTC_maxleafN.text()))==float(self.DTC_maxleafN.text()) and int(float(self.DTC_maxleafN.text()))>=1:
                    dict_model["DTC"]["max_leaf_nodes"] = int(float(self.DTC_maxleafN.text()))
                else :
                    QMessageBox.critical(self, "max_leaf_nodes correspond au nombre maximal de nœuds dans l'arbre. C'est un entier supérieur ou égal à 1 ou bien il prend la valeur None si vous ne souhaitez pas de limite.")

                # Verification of the parameter Max Dept
                if self.DTC_maxd.text()=='':
                    QMessageBox.critical(self,"Erreur de paramètre",
                                         "max_depth est vide.\nmax_depth correspond au nombre maximal de niveaux de nœuds dans l'arbre. C'est un entier supérieur ou égal à 1 ou bien il prend la valeur None si vous ne souhaitez pas de limite.")
                elif self.DTC_maxd.text()=='None':
                    dict_model["DTC"]["max_depth"] = None
                elif int(float(self.DTC_maxd.text()))==float(self.DTC_maxd.text()) and int(float(self.DTC_maxd.text()))>=1:
                    dict_model["DTC"]["max_depth"] = int(float(self.DTC_maxd.text()))
                else:
                    QMessageBox.critical(self,
                                         "max_depth correspond au nombre maximal de niveaux de nœuds dans l'arbre. C'est un entier supérieur ou égal à 1 ou bien il prend la valeur None si vous ne souhaitez pas de limite.")
                # Verification of the parameter Min Sample Split
                if self.DTC_mss.text()=='':
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "min_samples_split est vide.\nmin_samples_split est soit un entier supérieur à 2 et dans ce cas, il correspond au nombre minumum nécessaire à la création d'un nœud. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer un nœud. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer un nœud.")
                elif self.DTC_mss.text()=='None':
                    dict_model["DTC"]["min_samples_split"] = None
                elif int(float(self.DTC_mss.text()))==float(self.DTC_mss.text()) and int(float(self.DTC_mss.text()))>=1:
                    dict_model["DTC"]["min_samples_split"] = int(float(self.DTC_mss.text()))
                elif float(self.DTC_mss.text())<=1 and float(self.DTC_mss.text())>0:
                    dict_model["DTC"]["min_samples_split"] = float(self.DTC_mss.text())
                else:
                    QMessageBox.critical(self, "Erreur de paramètre",
                                         "min_samples_split est soit un entier supérieur à 2 et dans ce cas, il correspond au nombre minumum nécessaire à la création d'un nœud. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer un nœud. Soit un réel entre 0 et 1 qui correspond à une fraction minimum du nombre d'observations qu'il faut pour pouvoir créer un nœud.")

        self.close()
        self.trigger_model.emit(dict_model)


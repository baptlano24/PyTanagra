# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_quant.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Model_quanti(object):
    def setupUi(self, Model_quanti):
        Model_quanti.setObjectName("Model_quanti")
        Model_quanti.resize(795, 306)
        self.gridLayout = QtWidgets.QGridLayout(Model_quanti)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Model_quanti)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Model_quanti)
        self.label.setMaximumSize(QtCore.QSize(16777215, 67))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Model_quanti)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.SVR_use = QtWidgets.QCheckBox(Model_quanti)
        self.SVR_use.setObjectName("SVR_use")
        self.verticalLayout.addWidget(self.SVR_use, 0, QtCore.Qt.AlignHCenter)
        self.SVR_auto = QtWidgets.QCheckBox(Model_quanti)
        self.SVR_auto.setObjectName("SVR_auto")
        self.verticalLayout.addWidget(self.SVR_auto, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(Model_quanti)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(Model_quanti)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.combo_kernel = QtWidgets.QComboBox(Model_quanti)
        self.combo_kernel.setObjectName("combo_kernel")
        self.combo_kernel.addItem("")
        self.combo_kernel.addItem("")
        self.combo_kernel.addItem("")
        self.combo_kernel.addItem("")
        self.combo_kernel.addItem("")
        self.horizontalLayout_3.addWidget(self.combo_kernel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(Model_quanti)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.SVR_c = QtWidgets.QLineEdit(Model_quanti)
        self.SVR_c.setObjectName("SVR_c")
        self.horizontalLayout.addWidget(self.SVR_c)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(Model_quanti)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.SVR_degree = QtWidgets.QLineEdit(Model_quanti)
        self.SVR_degree.setObjectName("SVR_degree")
        self.horizontalLayout_2.addWidget(self.SVR_degree)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LR_use = QtWidgets.QCheckBox(Model_quanti)
        self.LR_use.setObjectName("LR_use")
        self.verticalLayout_3.addWidget(self.LR_use, 0, QtCore.Qt.AlignHCenter)
        self.LR_auto = QtWidgets.QCheckBox(Model_quanti)
        self.LR_auto.setObjectName("LR_auto")
        self.verticalLayout_3.addWidget(self.LR_auto, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(Model_quanti)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.LR_size = QtWidgets.QLineEdit(Model_quanti)
        self.LR_size.setObjectName("LR_size")
        self.horizontalLayout_4.addWidget(self.LR_size)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(Model_quanti)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_3 = QtWidgets.QRadioButton(Model_quanti)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_4.addWidget(self.radioButton_3)
        self.checkBox_2 = QtWidgets.QCheckBox(Model_quanti)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 2, 1)

        self.retranslateUi(Model_quanti)
        self.buttonBox.accepted.connect(Model_quanti.accept)
        self.buttonBox.rejected.connect(Model_quanti.reject)
        QtCore.QMetaObject.connectSlotsByName(Model_quanti)

    def retranslateUi(self, Model_quanti):
        _translate = QtCore.QCoreApplication.translate
        Model_quanti.setWindowTitle(_translate("Model_quanti", "Model Menu"))
        self.label.setText(_translate("Model_quanti", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Linear Regression</span></p></body></html>"))
        self.label_7.setText(_translate("Model_quanti", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Regression Tree</span></p></body></html>"))
        self.SVR_use.setText(_translate("Model_quanti", "Use ?"))
        self.SVR_auto.setText(_translate("Model_quanti", "Auto "))
        self.label_3.setText(_translate("Model_quanti", "Hyperparamètre :"))
        self.label_6.setText(_translate("Model_quanti", "<html><head/><body><p align=\"center\">Kernel:</p></body></html>"))
        self.combo_kernel.setItemText(0, _translate("Model_quanti", "linear"))
        self.combo_kernel.setItemText(1, _translate("Model_quanti", "poly"))
        self.combo_kernel.setItemText(2, _translate("Model_quanti", "rbf"))
        self.combo_kernel.setItemText(3, _translate("Model_quanti", "sigmoid"))
        self.combo_kernel.setItemText(4, _translate("Model_quanti", "precomputed"))
        self.label_4.setText(_translate("Model_quanti", "C :"))
        self.label_5.setText(_translate("Model_quanti", "Degree :"))
        self.LR_use.setText(_translate("Model_quanti", "Use ?"))
        self.LR_auto.setText(_translate("Model_quanti", "Auto "))
        self.label_8.setText(_translate("Model_quanti", "test_size:"))
        self.label_2.setText(_translate("Model_quanti", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Support Vector Regression </span></p></body></html>"))
        self.radioButton_3.setText(_translate("Model_quanti", "Use ?"))
        self.checkBox_2.setText(_translate("Model_quanti", "Auto "))


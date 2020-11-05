# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Select_Var.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(841, 627)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.target_push = QtWidgets.QPushButton(Dialog)
        self.target_push.setObjectName("target_push")
        self.verticalLayout_2.addWidget(self.target_push)
        self.target_cancel = QtWidgets.QPushButton(Dialog)
        self.target_cancel.setObjectName("target_cancel")
        self.verticalLayout_2.addWidget(self.target_cancel)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.Features = QtWidgets.QListView(Dialog)
        self.Features.setObjectName("Features")
        self.gridLayout.addWidget(self.Features, 1, 0, 1, 1)
        self.Variables = QtWidgets.QListView(Dialog)
        self.Variables.setObjectName("Variables")
        self.gridLayout.addWidget(self.Variables, 1, 3, 1, 1)
        self.Target = QtWidgets.QListView(Dialog)
        self.Target.setObjectName("Target")
        self.gridLayout.addWidget(self.Target, 1, 5, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 4, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.feature_push = QtWidgets.QPushButton(Dialog)
        self.feature_push.setObjectName("feature_push")
        self.verticalLayout.addWidget(self.feature_push)
        self.feature_cancel = QtWidgets.QPushButton(Dialog)
        self.feature_cancel.setObjectName("feature_cancel")
        self.verticalLayout.addWidget(self.feature_cancel)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Variable"))
        self.target_push.setText(_translate("Dialog", "=>"))
        self.target_cancel.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Features"))
        self.label_2.setText(_translate("Dialog", "Variables"))
        self.label_3.setText(_translate("Dialog", "Targets"))
        self.feature_push.setText(_translate("Dialog", "<="))
        self.feature_cancel.setText(_translate("Dialog", "X"))


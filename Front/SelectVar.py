from PyQt5.QtCore import QStringListModel, pyqtSignal
from Front.ui_SelectVar import Ui_Dialog
from PyQt5 import QtWidgets


class SelectVar(QtWidgets.QDialog, Ui_Dialog):
    trigger = pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super(SelectVar, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Target.setModel(QStringListModel())
        self.Features.setModel(QStringListModel())
        self.feature_push.clicked.connect(self.add_feature)
        self.target_push.clicked.connect(self.add_target)
        self.feature_cancel.clicked.connect(self.cancel_feature)
        self.target_cancel.clicked.connect(self.cancel_target)
        self.buttonBox.accepted.connect(self.accept_value)

    def add_target(self):
        cu_data = self.Variables.currentIndex().data()
        list_va = self.Target.model().stringList()
        list_va.append(cu_data)
        self.Target.model().setStringList((list(set(list_va))))

    def add_feature(self):
        cu_data = self.Variables.currentIndex().data()
        list_va = self.Features.model().stringList()
        list_va.append(cu_data)
        self.Features.model().setStringList((list(set(list_va))))

    def cancel_feature(self):
        cu_data = self.Variables.currentIndex().data()
        list_va = self.Features.model().stringList()
        list_va = [x for x in list_va if x != cu_data]
        self.Features.model().setStringList((list(set(list_va))))

    def cancel_target(self):
        cu_data = self.Target.currentIndex().data()
        list_va = self.Target.model().stringList()
        list_va = [x for x in list_va if x != cu_data]
        self.Target.model().setStringList((list(set(list_va))))

    def accept_value(self):
        tar_name = self.Target.model().stringList()
        fea_name = self.Features.model().stringList()
        self.close()
        self.trigger.emit([tar_name, fea_name])





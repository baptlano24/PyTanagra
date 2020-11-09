from PyQt5.QtCore import QStringListModel, pyqtSignal
from Front.ui_SelectVar import Ui_Dialog
from PyQt5 import QtWidgets


class SelectVar(QtWidgets.QDialog, Ui_Dialog):
    """Menu used to select the features and target of a data"""
    trigger = pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super(SelectVar, self).__init__(*args, **kwargs)
        # Initializing from ui.file (designer)
        self.setupUi(self)
        # Initializing the Features and Target Columns
        self.Target.setModel(QStringListModel())
        self.Features.setModel(QStringListModel())
        # When button are clicked
        self.feature_push.clicked.connect(self.add_feature)
        self.target_push.clicked.connect(self.add_target)
        self.feature_cancel.clicked.connect(self.cancel_feature)
        self.target_cancel.clicked.connect(self.cancel_target)
        # When the Users clicked on the button "Ok"
        self.buttonBox.accepted.connect(self.accept_value)

    def add_target(self):
        """Clean Target List,Add a column name from Variables List to Target List """
        self.Target.setModel(QStringListModel())
        cu_data = self.Variables.currentIndex().data()
        list_va = self.Target.model().stringList()
        list_va.append(cu_data)
        self.Target.model().setStringList((list(set(list_va))))

    def add_feature(self):
        """Add a column name from Variables List to Features List """
        cu_data = self.Variables.currentIndex().data()
        list_va = self.Features.model().stringList()
        list_va.append(cu_data)
        self.Features.model().setStringList((list(set(list_va))))

    def cancel_feature(self):
        """ Remove Feature from Features List """
        cu_data = self.Variables.currentIndex().data()
        list_va = self.Features.model().stringList()
        list_va = [x for x in list_va if x != cu_data]
        self.Features.model().setStringList((list(set(list_va))))

    def cancel_target(self):
        """ Remove Target from Target List """
        cu_data = self.Target.currentIndex().data()
        list_va = self.Target.model().stringList()
        list_va = [x for x in list_va if x != cu_data]
        self.Target.model().setStringList((list(set(list_va))))

    def accept_value(self):
        """When the user clicked pn "Ok" => send the information
        from target and features as Signal"""
        tar_name = self.Target.model().stringList()
        fea_name = self.Features.model().stringList()
        self.close()
        self.trigger.emit([tar_name, fea_name])

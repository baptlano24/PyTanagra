from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QFormLayout, \
    QMainWindow, QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sn
from sklearn import preprocessing


class Window_Quant(QMainWindow):
    "svr.get_params(), svr.score(X_test, Y_test), graphs, end - start"
    def __init__(self, parent=None, data=None, dict=None):
        super(Window_Quant, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()
        self.table = QTableWidget()
        self.data = data
        self.dict = dict
        self.accuracy = None
        self.table_model = QTableWidget()
        self.info_model = None

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        mtitle = QLabel('Model Conclusion', self)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        layout.addWidget(mtitle)
        layout.addWidget(self.table_model)
        layout.addWidget(self.canvas)
        wid.setLayout(layout)

    def upload_model(self):
        self.table_model.setColumnCount(len(self.info_model))
        self.table_model.setRowCount(1)
        self.table_model.setHorizontalHeaderLabels(list(self.info_model.keys()))
        for column, key in enumerate(self.info_model):
            new_item = QTableWidgetItem(str(self.info_model[key]))
            self.table_model.setItem(0, column, new_item)

    def setData(self, model,score, graph, time):

        self.data = graph
        self.info_model = model
        self.info_model["time"] = time
        self.info_model["R2"] = score
        self.upload_model()
        self.plot()

    def plot(self):
        le = preprocessing.LabelEncoder()
        self.figure.clear()
        ax = (ax1, ax2) = self.figure.subplots(1, 2)

        ax1.set_title("Regression", fontsize=15)
        ax1.scatter(self.data["X_1"], self.data["Y"],marker='o',c='b',label='Raw data')
        ax1.plot(self.data["X_1"], self.data["Y_pred"],'r-',label='Prediction')
        ax1.set_xlabel('X_1',fontsize=10)
        plt.setp(ax1.get_xticklabels(), fontsize=10)
        ax1.legend()

        min_Y=min(self.data["Y"])
        max_Y=max(self.data["Y"])
        ax2.set_title("Y_pred vs. Y", fontsize=15)
        ax2.plot([min_Y,max_Y],[min_Y,max_Y],ls='-',c='r')
        ax2.scatter(self.data["Y"], self.data["Y_pred"],marker='.',c='b')
        ax2.set_xlabel('Y',fontsize=10)
        ax2.set_ylabel('Y_pred',fontsize=10)
        plt.setp(ax2.get_xticklabels(), fontsize=10)
        plt.setp(ax2.get_yticklabels(), fontsize=10)

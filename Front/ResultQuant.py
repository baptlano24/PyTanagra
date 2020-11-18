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
        # TODO FAIRE LEGENDE + CHANGE COLORATION
        le = preprocessing.LabelEncoder()
        self.figure.clear()
        ax = (ax1, ax2) = self.figure.subplots(1, 2)
        ax2.set_title("Predicted Classification", fontsize=10)
        ax1.set_title("Real Classification", fontsize=10)
        print(len(self.data["X_1"]), len(self.data["Y"]))
        print(len(self.data["X_1"]), len(self.data["Y_pred"]))
        y = ax1.scatter(self.data["X_1"], self.data["Y"])
        y1 = ax2.scatter(self.data["X_1"], self.data["Y_pred"])


from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QFormLayout, \
    QMainWindow, QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sn
from sklearn import preprocessing

class Window(QMainWindow):
    def __init__(self, parent=None, data=None, dict=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()
        self.pca = None
        self.figure_pca = plt.figure()
        self.table = QTableWidget()
        self.data = data
        self.dict = dict
        self.accuracy = None
        self.table_model = QTableWidget()
        self.info_model = None

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.canvas_pca = FigureCanvas(self.figure_pca)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        mtitle = QLabel('Model Conclusion', self)
        conf_mat = QLabel('Confusion Matrix', self)
        pca_score = QLabel('PCA graph', self)
        score = QLabel('Score Table', self)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        layout.addWidget(mtitle)
        layout.addWidget(self.table_model)
        layout.addWidget(conf_mat)
        layout.addWidget(self.canvas)
        layout.addWidget(pca_score)
        layout.addWidget(self.canvas_pca)
        layout.addWidget(score)
        layout.addWidget(self.table)
        wid.setLayout(layout)

    def upload_table(self):
        self.accuracy = self.dict.pop("accuracy", None)
        self.info_model["accuracy"] = self.accuracy
        self.table.setColumnCount(len(list(self.dict["weighted avg"].keys())))
        self.table.setRowCount(len(self.dict))
        self.table.setHorizontalHeaderLabels(list(self.dict["weighted avg"].keys()))
        self.table.setVerticalHeaderLabels(list(self.dict.keys()))
        for row, key in enumerate(self.dict):
            for column, item in enumerate(self.dict[key]):
                new_item = QTableWidgetItem(str(self.dict[key][item]))
                self.table.setItem(row, column, new_item)

    def upload_model(self):
        self.table_model.setColumnCount(len(self.info_model))
        self.table_model.setRowCount(1)
        self.table_model.setHorizontalHeaderLabels(list(self.info_model.keys()))
        for column, key in enumerate(self.info_model):
            new_item = QTableWidgetItem(str(self.info_model[key]))
            self.table_model.setItem(0, column, new_item)

    def setData(self, model, matrix, dict_cr, graph, time):

        self.data = matrix
        self.pca = graph
        self.dict = dict_cr
        self.info_model = model
        self.info_model["time"] = time
        self.upload_table()
        self.upload_model()
        self.plot()
        self.plot_pca()

    def plot(self):
        ''' plot some random stuff '''
        # TODO CHANGE COLORATION

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above
        sn.set(font_scale=1.4)  # for label size
        sn.heatmap(self.data, annot=True, annot_kws={"size": 10}, ax=ax)  # font size
        # plot data
        # ax.plot(data, '*-')
        self.canvas.draw()

    def plot_pca(self):
        #TODO FAIRE LEGENDE + CHANGE COLORATION
        le = preprocessing.LabelEncoder()
        le.fit(self.pca["Y"])
        Y_encode = le.transform(self.pca["Y"])
        Y1_encode = le.transform(self.pca["Y_pred"])
        self.figure_pca.clear()
        ax = (ax1, ax2) = self.figure_pca.subplots(1, 2)
        ax2.set_title("Predicted Classification", fontsize=10)
        ax1.set_title("Real Classification",fontsize=10)
        y = ax1.scatter(self.pca["ACP_0"], self.pca["ACP_1"], c=Y_encode)
        y1 = ax2.scatter(self.pca["ACP_0"], self.pca["ACP_1"], c=Y1_encode)


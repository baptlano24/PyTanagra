
from PyQt5.QtWidgets import  QVBoxLayout, QTableWidget, QTableWidgetItem,QMainWindow, QWidget, QTabWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sn
from sklearn import preprocessing
import matplotlib.lines as mlines


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
        tabWidget = QTabWidget()
        tabWidget.addTab(self.table_model,'Model Conclusion')
        tabWidget.addTab(self.canvas,'Confusion Matrix')
        tabWidget.addTab(self.canvas_pca,'PCA graph')
        tabWidget.addTab(self.table,'Score Table')
        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        layout.addWidget(tabWidget)
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

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above
        sn.set(font_scale=1.4)  # for label size
        sn.heatmap(self.data, annot=True, annot_kws={"size": 10}, ax=ax,cmap=plt.cm.Blues,cbar_kws={'label': 'Number of elements'})
        ax.figure.axes[-1].yaxis.label.set_size(10)
        # plot data
        # ax.plot(data, '*-')
        self.canvas.draw()

    def plot_pca(self):
        new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                      '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                      '#bcbd22', '#17becf']

        le = preprocessing.LabelEncoder()
        le.fit(self.pca["Y"])
        Y_encode = [new_colors[e%10] for e in le.transform(self.pca["Y"])]
        Y1_encode = [new_colors[e%10] for e in le.transform(self.pca["Y_pred"])]

        #Creation of the legend
        unique_lab = list(set(self.pca["Y"]))
        unique_num= list(set(le.transform(self.pca["Y"])))
        print(unique_lab,unique_num)
        unique_color = [new_colors[e % 10] for e in unique_num]
        list_leg=[]
        for i in range(len(unique_lab)):
            list_leg.append(mlines.Line2D([], [], color=unique_color[i], marker='o', ls='', label=unique_lab[i]))

        self.figure_pca.clear()
        ax = (ax1, ax2) = self.figure_pca.subplots(1, 2)

        ax1.set_title("Real Classification",fontsize=15)
        ax1.scatter(self.pca["ACP_0"], self.pca["ACP_1"], c=Y_encode)
        ax1.set_xlabel("First axis of the PCA",fontsize=10)
        ax1.set_ylabel("Second axis of the PCA",fontsize=10)
        plt.setp(ax1.get_xticklabels(), fontsize=10)
        plt.setp(ax1.get_yticklabels(), fontsize=10)
        ax1.legend(handles=list_leg)

        ax2.set_title("Predicted Classification", fontsize=15)
        ax2.scatter(self.pca["ACP_0"], self.pca["ACP_1"], c=Y1_encode)
        ax2.set_xlabel("First axis of the PCA",fontsize=10)
        ax2.set_ylabel("Second axis of the PCA",fontsize=10)
        plt.setp(ax2.get_xticklabels(), fontsize=10)
        plt.setp(ax2.get_yticklabels(), fontsize=10)

        ax2.legend(handles=list_leg)


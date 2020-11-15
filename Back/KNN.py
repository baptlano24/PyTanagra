from time import perf_counter
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


def knn_class(x, y, auto=True, params=None):
    start = perf_counter()
    scalar = StandardScaler()
    scalar.fit(x)
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3)
    scalar.fit(X_train)
    X_train = scalar.transform(X_train)
    X_test = scalar.transform(X_test)

    if auto:
        leaf_size = np.arange(1, 30)
        n_neighbors = np.arange(1, 20)
        distance = ["euclidean", "manhattan", "chebyshev", "minkowski"]
        p = [1, 2]
        parameter = dict(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p, metric=distance)
        knn = KNeighborsClassifier()
        clf = GridSearchCV(knn, parameter, cv=3, n_jobs=-1)
        best_model = clf.fit(X_train, Y_train)
        end = perf_counter()
        return best_model.best_params_, best_model.best_score_, best_model.predict(X_test), end-start
    else:
        [leaf_size, n_neighbors, p, metric] = params
        knn_1 = KNeighborsClassifier(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p, metric=metric, n_jobs=-1)
        knn_1.fit(X_train, Y_train)
        y_pred = knn_1.predict(X_test)
        cm = confusion_matrix(Y_test, y_pred)
        cr = classification_report(Y_test, y_pred)
        end1 = perf_counter()
        return knn_1.get_params(), cm, cr, y_pred, end1-start


#df = pd.read_csv('C:/Users/bapti/OneDrive/Bureau/SISE/Machine Learning Python/data_breast_cancer.csv', encoding='latin-1', sep=',')
#del df['id']
#del df['Unnamed: 32']
#X = df.iloc[:,1:len(df.columns)]
#Y = df.iloc[:,0]
#X = np.array(X)
#Y = np.array(Y)
#print(X,X.shape)
#print(Y,Y.shape)
#params = [5, 4, 1, "euclidean"]
#print(knn_class(X,Y,auto=True,params=params))

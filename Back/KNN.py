from time import perf_counter
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA


def knn_class(x, y, auto=True, params=None):
    start = perf_counter()
    label_list = list(set(y))

    if auto:
        leaf_size = np.arange(1, 30)
        n_neighbors = np.arange(1, 20)
        distance = ["euclidean", "manhattan", "chebyshev", "minkowski"]
        p = [1, 2]
        parameter = dict(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p, metric=distance)
        knn = KNeighborsClassifier()
        clf = GridSearchCV(knn, parameter, cv=3, n_jobs=-1)
        best_model = clf.fit(x, y)
        Y_pred=best_model.predict(x)

        cm = confusion_matrix(x, y,labels=label_list)
        cr = classification_report(y, Y_pred,target_names=label_list, output_dict=True)

        pca = PCA(n_components=2)
        acp = pca.fit_transform(x)

        graphs = {'ACP_0': acp[:, 0], 'ACP_1': acp[:, 1], 'Y': y, 'Y_pred': Y_pred}
        df_cm = pd.DataFrame(cm, index=label_list,
                             columns=label_list).transpose()

        end = perf_counter()
        return best_model.best_params_,df_cm, cr, graphs, end-start
    else:
        scalar = StandardScaler()
        scalar.fit(x)
        X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3)
        scalar.fit(X_train)
        X_train = scalar.transform(X_train)
        X_test = scalar.transform(X_test)

        [leaf_size, n_neighbors, p, metric] = params
        knn_1 = KNeighborsClassifier(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p, metric=metric, n_jobs=-1)
        knn_1.fit(X_train, Y_train)
        y_pred = knn_1.predict(X_test)

        pca = PCA(n_components=2)
        acp = pca.fit_transform(X_test)
        graphs = {'ACP_0': acp[:, 0], 'ACP_1': acp[:, 1], 'Y': Y_test, 'Y_pred': y_pred}

        cm = confusion_matrix(Y_test, y_pred, labels=label_list)
        cr = classification_report(Y_test, y_pred,target_names=label_list, output_dict=True)
        end1 = perf_counter()
        df_cm = pd.DataFrame(cm, index=label_list,
                             columns=label_list).transpose()
        return knn_1.get_params(), df_cm, cr, graphs, end1-start


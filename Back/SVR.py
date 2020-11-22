# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:47:38 2020

@author: Romain Pic
"""

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error, make_scorer
from time import perf_counter

def SVR_b(X,Y,auto=True,params=None):
    """
    Parameters
    ----------
    X : numpy array or pandas DataFrame
        Entries to link to the target variable.
    Y : numpy array or time series
        Target variable.
    auto : BOOLEAN, optional
        if TRUE the function will perform a cross-validation to find the optimal parameters for the SVM Regression
        otherwise the user has to specify the parameters used. The default is True.
    params : LIST of length 2 or 3, optional
        C - regularisation parameter (float>=0),
        kernel - type of kernel used among : 'linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed',
        degree - degree of the ploynomial kernel. The default is None.

    Returns
    -------
    DICT,FLOAT,NUMPY ARRAY
    Parameters of the chosen model (the best or the one chosen by the user),
    Score of the chosen model,
    Values predicted by the model.
    """
    start = perf_counter()
    if not(auto):
        if len(params)==2:
            [C,k]=params
        else:
            [C,k,deg]=params
        if k=='linear':
            svr = SVR(kernel=k,C=C)
        else:
            svr = SVR(kernel=k,degree=deg,C=C)
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)
        svr.fit(X_train,Y_train)

        Y_pred=svr.predict(X_test)

        graphs={'X_1':X_test[:,0],'Y':Y_test,'Y_pred':Y_pred}
        end=perf_counter()
        return svr.get_params(),mean_squared_error(Y_test,Y_pred),graphs,end-start
    else:

        scorer = make_scorer(mean_squared_error)
        svr = SVR()
        params = {'C':[1,2,3],'kernel':['linear','poly','rbf'],'degree':[2,3]}
        reg = GridSearchCV(svr, param_grid=params, cv=10, scoring=scorer)
        reg.fit(X,Y)

        Y_pred=reg.predict(X)

        graphs = {'X_1': X[:, 0], 'Y': Y, 'Y_pred': Y_pred}
        end = perf_counter()
        return reg.best_params_,reg.best_score_,graphs,end-start
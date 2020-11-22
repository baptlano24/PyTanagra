# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 09:52:48 2020

@author: Romain Pic
"""
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, make_scorer
from time import perf_counter


def RegTree(X, Y, auto=True, params=None):
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
        criterion -  criterion to split nodes among : 'mse', 'friedman_mse', 'mae'
        max_depth - Maximal depth of the tree
        min_samples_split - Number of minimal elements to create a node. Can also be a float between 0 and 1, it is the minimal fraction of the total population necessary to create a node.
        min_samples_leaf - Number of minimal elements to create a leaf. Can also be a float between 0 and 1, it is the minimal fraction of the total population necessary to create a leaf.
    Returns
    -------
    DICT,FLOAT,NUMPY ARRAY
    Parameters of the chosen model (the best or the one chosen by the user),
    Score of the chosen model,
    Values predicted by the model.
    """
    start = perf_counter()
    if not (auto):
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
        [criterion, min_split, min_leaf] = params

        tree = DecisionTreeRegressor(criterion=criterion, min_samples_split=min_split, min_samples_leaf=min_leaf)
        tree.fit(X_train, Y_train)

        Y_pred = tree.predict(X_test)

        graphs = {'X_1': X_test[:, 0], 'Y': Y_test, 'Y_pred': Y_pred}
        end = perf_counter()

        return tree.get_params(), mean_squared_error(Y_test, Y_pred), graphs, end - start
    else:
        params = {'criterion': ['mse', 'friedman_mse', 'mae'],
                  'max_depth': [None],
                  'min_samples_split': [2, 0.05, 0.02],  # 2, 5%, 2%
                  'min_samples_leaf': [1, 0.01, 0.02]}  # 1, 1%, 2%
        scorer = make_scorer(mean_squared_error)  # default score
        tree = DecisionTreeRegressor()
        reg = GridSearchCV(tree, param_grid=params, cv=10, scoring=scorer)
        reg.fit(X, Y)

        Y_pred = reg.predict(X)

        graphs = {'X_1': X[:, 0], 'Y': Y, 'Y_pred': Y_pred}
        end = perf_counter()
        return reg.best_params_, reg.best_score_, graphs, end - start

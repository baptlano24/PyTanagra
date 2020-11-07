# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:47:38 2020

@author: Romain Pic
"""

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, make_scorer
import pandas as pd
import matplotlib.pyplot as plt

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
    FLOAT,FLOAT,NUMPY ARRAY
    Parameters of the chosen model (the best or the one chosen by the user),
    Score of the chosen model,
    Values predicted by the model.
    """
<<<<<<< Updated upstream
    
    if not(auto):
        p=list(params)
        if len(p)==2:
            [C,k]=p
        else:
            [C,k,deg]=p
        if k=='linear':
            svr = SVR(kernel=k,C=C)
        else:
            svr = SVR(kernel=k,degree=deg,C=C)
        svr.fit(X,Y)

        print(svr.get_params())
        print(svr.score(X,Y))
        
        Y_pred=svr.predict(X)
=======
    model = 1
    if not(auto):
        []=list(params)
>>>>>>> Stashed changes
        
        fig1=plt.figure()
        plt.scatter(Y,Y_pred,marker='.')
        plt.xlabel('y')
        plt.ylabel('Y_pred')
        
        fig2=plt.figure()
        plt.scatter(X[:,0],Y_pred,marker='.',c='r',label='Y_pred')
        plt.scatter(X[:,0],Y,marker='.',c='b',label='Y')
        plt.xlabel('X_1')
        plt.legend()
        return (svr.get_params(),svr.score(X,Y),svr.predict(X))
    else:
        
        scorer = make_scorer(r2_score)
        svr = SVR()
        params = {'C':[1,2,3],'kernel':['linear','poly','rbf'],'degree':[2,3]}
        reg = GridSearchCV(svr, param_grid=params, cv=10, scoring=scorer ,n_jobs=-1)
        reg.fit(X,Y)
        
        print(reg.cv_results_['mean_test_score']) #Scores comparés
        print(reg.best_params_) #Meilleures valeurs de paramètres
        print(reg.best_score_) #Meilleur score
        
        
        Y_pred=reg.predict(X)
        
        fig1=plt.figure()
        plt.scatter(Y,Y_pred,marker='.')
        plt.xlabel('y')
        plt.ylabel('Y_pred')
        
        fig2=plt.figure()
        plt.scatter(X[:,0],Y_pred,marker='.',c='r',label='Y_pred')
        plt.scatter(X[:,0],Y,marker='.',c='b',label='Y')
        plt.xlabel('X_1')
        plt.legend()
        
        return (reg.best_params_,reg.best_score_,reg.predict(X))
 
###Test
# import numpy as np


# dur=5
# t = np.arange(0,dur,0.01)

# sinusoid = np.transpose(2*t)
# t= np.transpose(np.array([t,t**2]))
# sinusoid=np.random.normal(0,1,sinusoid.shape)+sinusoid
# p=[1.0,'linear']
# print(SVR_b(X=t,Y=sinusoid,auto=False,params=p))
 
 
# # df=pd.read_csv('data_breast_cancer.csv',encoding='latin-1',sep=',')
# # df['diagnosis']=(df['diagnosis']=='M').astype(int)
# # del df['id']
# # del df['Unnamed: 32']
# # X=df.iloc[:,2:len(list(df.columns))]
# # Y=df.iloc[:,1]



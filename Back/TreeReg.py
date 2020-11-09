# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 09:52:48 2020

@author: Romain Pic
"""
from sklearn.model_selection import GridSearchCV,train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, make_scorer
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def RegTree(X,Y,auto=True,params=None):
    
    if not(auto):
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)
        [criterion,min_split,min_leaf]=list(params)
        
        tree = DecisionTreeRegressor(criterion=criterion, min_samples_split=min_split, min_samples_leaf=min_leaf)
        tree.fit(X_train,Y_train)
        
        
        Y_pred=tree.predict(X_test)
        print(tree.get_params())
        print(mean_squared_error(Y_test,Y_pred))
        
        fig1=plt.figure()
        plt.scatter(Y_test,Y_pred,marker='.')
        plt.xlabel('Y_test')
        plt.ylabel('Y_pred')
        
        fig2=plt.figure()
        plt.scatter(X_test[:,0],Y_pred,marker='.',c='r',label='Y_pred')
        plt.scatter(X_test[:,0],Y_test,marker='.',c='b',label='Y_test')
        plt.xlabel('X_1')
        plt.legend()
        
        return (tree.get_params(),mean_squared_error(Y_test,Y_pred),Y_pred)
    else:
        params = {'criterion':['mse','friedman_mse','mae'],
                  'max_depth':[None],
                  'min_samples_split':[2,int(len(X)/20),int(len(X)/50)],#2, 5%, 2%
                  'min_samples_leaf':[1,int(len(X)/100),int(len(X)/50)]}#1, 1%, 2%
        scorer = make_scorer(mean_squared_error)#default score
        tree = DecisionTreeRegressor()
        reg = GridSearchCV(tree, param_grid=params, cv=10, scoring=scorer, n_jobs=-1)
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
import numpy as np


dur=5
t = np.arange(0,dur,0.01)

sinusoid = np.transpose(2*t)
t= np.transpose(np.array([t,t**2]))
sinusoid=np.random.normal(0,1,sinusoid.shape)+sinusoid
p=['friedman_mse',2,1]
print(RegTree(X=t,Y=sinusoid,auto=False,params=p))
 
 
# df=pd.read_csv('data_breast_cancer.csv',encoding='latin-1',sep=',')
# df['diagnosis']=(df['diagnosis']=='M').astype(int)
# del df['id']
# del df['Unnamed: 32']
# X=df.iloc[:,2:len(list(df.columns))]
# Y=df.iloc[:,1]
        
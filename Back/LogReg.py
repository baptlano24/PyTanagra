# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:23:20 2020

@author: Romain Pic
"""


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import f1_score, make_scorer,confusion_matrix, classification_report
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from time import perf_counter

def LogReg(X,Y,auto=True,params=None):

    """
    X : numpy array or pandas DataFrame
        Entries to link to the target variable.
    Y : numpy array or time series
        Target variable, category to predict.
    auto : BOOLEAN, optional
        if TRUE the function will perform a cross-validation to find the optimal parameters for the Logistic Regression
        otherwise the user has to specify the parameters used. The default is True.
    params : LIST of length 2, optional
        C - regularisation parameter (float>=0),
        penalty - type of penalty used among : 'none’, ‘l1’, ‘l2’, ‘elasticnet’.The default is None.
    Returns
    -------
    DICT,FLOAT,NUMPY ARRAY
    Parameters of the chosen model (the best or the one chosen by the user),
    Score of the chosen model,
    Values predicted by the model.
    """
    start=perf_counter()
    label_list = list(set(Y))
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
    if not(auto):
        [C,penalty]=list(params)
        #X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)

        reg=LogisticRegression(solver="saga",penalty=penalty, C=C, n_jobs=-1)
        reg.fit(X_train,Y_train)
        Y_pred=reg.predict(X_test)

        pca = PCA(n_components=2)
        acp = pca.fit_transform(X_test)

        cm = confusion_matrix(Y_test, Y_pred,labels=label_list)
        cr = classification_report(Y_test, Y_pred,target_names=label_list, output_dict=True)

        ###Comparison of the best model with the actual classes using PCA
        #fig1, (ax1, ax2) = plt.subplots(1, 2,figsize=(10,5))

        #ax1.set_title("Vraie Classification")
        #ax1.scatter(temp[:,0],temp[:,1],c=Y_test,marker='.')

        #ax2.set_title("Classification prédite")
        #ax2.scatter(temp[:,0],temp[:,1],c=Y_pred,marker='.')

        #plt.suptitle("Classification représentée dans l'espace des deux premières composantes principales")

        ###Comparison of the best model with the actual classes in the real space
        #fig2, (ax1, ax2) = plt.subplots(1, 2,figsize=(10,5))

        #ax1.set_title("Vraie Classification")
        #ax1.scatter(X_test[:,0],X_test[:,1],c=Y_test,marker='.')

        #ax2.set_title("Classification prédite")
        #ax2.scatter(X_test[:,0],X_test[:,1],c=Y_pred,marker='.')

        #plt.suptitle("Classification représentée dans l'espace réel")
        graphs = {'ACP_0': acp[:, 0],'ACP_1': acp[:, 1], 'Y': Y_test, 'Y_pred': Y_pred}
        df_cm = pd.DataFrame(cm, index=label_list,
                             columns=label_list).transpose()
        end = perf_counter()
        return reg.get_params(),df_cm,cr,graphs,end-start
    else:
        print(Y[0],"Y")
        scorer = make_scorer(f1_score,pos_label=Y[0])
        modele = LogisticRegression(solver="saga")
        params = {'C':[0,0.5,1,2,3],'penalty':['l1','l2','elasticnet'],'l1_ratio': [0.5]}
        reg = GridSearchCV(modele, param_grid=params, cv=10, scoring=scorer,n_jobs=-1)
        reg.fit(X,Y)

        print(reg.cv_results_['mean_test_score']) #Scores comparés
        print(reg.best_params_) #Meilleures valeurs de paramètres
        print(reg.best_score_) #Meilleur score


        pca = PCA(n_components=2)
        acp = pca.fit_transform(X)

        Y_pred=reg.predict(X)
        cm = confusion_matrix(Y, Y_pred, labels=label_list)
        cr = classification_report(Y, Y_pred, target_names=label_list, output_dict=True)

        ###Comparison of the best model with the actual classes using PCA
        #fig1, (ax1, ax2) = plt.subplots(1, 2,figsize=(10,5))

        #ax1.set_title("Vraie Classification")
        #ax1.scatter(temp[:,0],temp[:,1],c=Y,marker='.')

        #ax2.set_title("Classification prédite")
        #ax2.scatter(temp[:,0],temp[:,1],c=Y_pred,marker='.')

        #plt.suptitle("Classification représentée dans l'espace des deux premières composantes principales")

        ###Comparison of the best model with the actual classes in the real space
        #fig2, (ax1, ax2) = plt.subplots(1, 2,figsize=(10,5))

        #ax1.set_title("Vraie Classification")
        #ax1.scatter(X[:,0],X[:,1],c=Y,marker='.')

        #ax2.set_title("Classification prédite")
        #ax2.scatter(X[:,0],X[:,1],c=Y_pred,marker='.')

        #plt.suptitle("Classification représentée dans l'espace réel")
        graphs = {'ACP_0': acp[:, 0],'ACP_1': acp[:, 1], 'Y': Y, 'Y_pred': Y_pred}
        end = perf_counter()
        df_cm = pd.DataFrame(cm, index=label_list,
                             columns=label_list).transpose()
        return reg.best_params_,df_cm,cr,graphs,end-start

###Test
# import numpy as np


# # dur=5
# # t = np.arange(0,dur,0.01)

# # sinusoid = np.transpose(2*t)
# # t= np.transpose(np.array([t,t**2]))
# # sinusoid=np.random.normal(0,1,sinusoid.shape)+sinusoid
# # p=[1.0,'linear']
# # print(SVR_b(X=t,Y=sinusoid))


# df=pd.read_csv('data_breast_cancer.csv',encoding='latin-1',sep=',')
# df['diagnosis']=(df['diagnosis']=='M').astype(int)
# del df['id']
# del df['Unnamed: 32']
# X=df.iloc[:,1:len(df.columns)]
# Y=df.iloc[:,0]
# X=np.array(X)
# Y=np.array(Y)

# p=[1,'l2']
# print(LogReg(X,Y,auto=False,params=p))

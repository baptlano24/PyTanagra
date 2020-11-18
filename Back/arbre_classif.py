import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer, f1_score, confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from time import time

def arbre_clas(X, y, Auto, nb_regle = None, profondeur = None, nb_indiv = None):
    # X = variables explicatives
    # y = variable cible
    #nb_regle = hyperparamètre correspondant au nombre de règles maximales de l'arbre
    #profondeur = hyperparamètre correspondant à la profondeur maximale de l'arbre
    #nb_indiv = hyperparamètre correspondant au nombre d'individus minimum pour qu'un sommet soit segmenté

    start = time()  # début du chrono
    label_list = list(set(y))
     #Recodage des variables qualitatives
    #var_quali = [var for var in X.columns[:] if X[var].dtype == np.object_]
    #var_quanti = [var for var in X.columns[:] if X[var].dtype != np.object_]
    #if len(var_quali) != 0:
        #recodage_quali = pd.get_dummies(X[var_quali])
        #var_exp = pd.concat([recodage_quali, X[var_quanti]], axis=1)
    #else:
        #var_exp = pd.DataFrame(X)
    #var_exp = pd.DataFrame(var_exp)

    # Echantillonage
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    taille_ech = X.shape[0]

    # Mode automatique --> Optimisation des hyper-paramètres
    if Auto:
        # Définition des données
        scorer = make_scorer(f1_score,pos_label=label_list[0])
        modele = DecisionTreeClassifier()
        params = {"max_leaf_nodes": list(range(2, 50)), "max_depth": [10, 20, 30], "min_samples_split": [int(taille_ech/10), int(taille_ech/20), int(taille_ech/30)]}

        # Instanciation et exécution
        search = GridSearchCV(modele, param_grid=params, cv=5, scoring=scorer)
        search.fit(X_train, y_train)

        # Récupération des sorties
        arbre = search.best_estimator_ # meilleur modèle

    # Si les hyper-paramètres ont été défini par l'utilisateur
    else:
        # Si l'utilisateur n'a pas renseigné nb_indiv, on estime le paramètre
        if nb_indiv == None:
            # Définition des données
            scorer = make_scorer(f1_score,pos_label=label_list[0])
            modele = DecisionTreeClassifier()
            params = {"min_samples_split": [int(taille_ech/10), int(taille_ech/20), int(taille_ech/30)]}
            # Instanciation et exécution
            search = GridSearchCV(modele, param_grid=params, cv=5, scoring=scorer)
            search.fit(X_train, y_train)
            # Récupération des sorties
            nb_indiv = search.best_params_.get("min_samples_split") #la meilleur valeur du parametre

        arbre = DecisionTreeClassifier(max_leaf_nodes=nb_regle, max_depth=profondeur, min_samples_split=nb_indiv)


    # Entrainement
    arbre.fit(X_train, y_train)
    #plt.figure()
    #plot_tree(arbre, feature_names=list(var_exp.columns[:]), filled=True)
    #plt.show()

    # Prediction
    pred = arbre.predict(X_test)

    # Evaluation
    report = metrics.classification_report(y_test, pred, target_names=label_list,output_dict=True)
    conf = confusion_matrix(y_test, pred,labels=label_list) #matrice de confusion

    pca = PCA(n_components=2)
    acp = pca.fit_transform(X_test)
    graphs = {'ACP_0': acp[:, 0], 'ACP_1': acp[:, 1], 'Y': y_test, 'Y_pred': pred}

    done = time()  # fin du chrono
    elapsed = done - start  # temps de calcul
    df_cm = pd.DataFrame(conf, index=label_list,
                         columns=label_list).transpose()
    return arbre.get_params(), df_cm, report, graphs, elapsed


# #Test
# data = pd.read_excel("C:/Users/Axelle/Desktop/M/03_SISE/heart.xlsx", sheet_name = 0)
# x_ = data.iloc[:,:13]
# y_ = pd.DataFrame(data.iloc[:,13])
# print(arbre_clas(x_, y_, True))
# #print(arbre_clas(x_, y_, False, profondeur=2, nb_indiv=30, nb_regle=5))
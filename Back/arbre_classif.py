import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer, f1_score, confusion_matrix
from sklearn import metrics
from sklearn.decomposition import PCA
from time import time


def arbre_clas(X, y, Auto, nb_regle=None, profondeur=None, nb_indiv=None):
    # X = features
    # y = target
    # nb_regle = maximal number of rules in the tree
    # profondeur = maximal depth of the tree
    # nb_indiv = minimal number of elements to create a leaf

    start = time()  # starting
    label_list = list(set(y))
    taille_ech = X.shape[0]

    # Auto mode --> Optimisation of params
    if Auto:
        # Creation of the model
        scorer = make_scorer(f1_score, pos_label=label_list[0])
        modele = DecisionTreeClassifier()
        params = {"max_leaf_nodes": list(range(2, 50)), "max_depth": [10, 20, 30],
                  "min_samples_split": [int(taille_ech / 10), int(taille_ech / 20), int(taille_ech / 30)]}

        # Cross-Validation
        search = GridSearchCV(modele, param_grid=params, cv=5, scoring=scorer)
        search.fit(X, y)
        # Best tree
        arbre = search.best_estimator_
        # Training
        arbre.fit(X, y)
        # Prediction
        pred = arbre.predict(X)

        # Evaluation
        report = metrics.classification_report(y, pred, target_names=label_list, output_dict=True)
        conf = confusion_matrix(y, pred, labels=label_list)

        pca = PCA(n_components=2)
        acp = pca.fit_transform(X)
        graphs = {'ACP_0': acp[:, 0], 'ACP_1': acp[:, 1], 'Y': y, 'Y_pred': pred}

    # Manual mode
    else:
        # Sampling
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        arbre = DecisionTreeClassifier(max_leaf_nodes=nb_regle, max_depth=profondeur, min_samples_split=nb_indiv)
        # Training
        arbre.fit(X, y)
        # Prediction
        pred = arbre.predict(X)

        # Evaluation
        report = metrics.classification_report(y_test, pred, target_names=label_list, output_dict=True)
        conf = confusion_matrix(y_test, pred, labels=label_list)

        pca = PCA(n_components=2)
        acp = pca.fit_transform(X_test)
        graphs = {'ACP_0': acp[:, 0], 'ACP_1': acp[:, 1], 'Y': y_test, 'Y_pred': pred}

    done = time()  # ending
    elapsed = done - start  # computation time
    df_cm = pd.DataFrame(conf, index=label_list,
                         columns=label_list).transpose()
    return arbre.get_params(), df_cm, report, graphs, elapsed

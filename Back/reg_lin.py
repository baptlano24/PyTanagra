from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
from time import time
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

def regression_lin(X, y, Auto, intercept = True, normal = False):
    # X = variables explicatives
    # y = variable cible

    start = time()  # début du chrono

    # Echantillonage
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Mode automatique --> Optimisation des hyper-paramètres
    if Auto:
        # Définition des données
        scorer = make_scorer(mean_squared_error)
        modele = LinearRegression()
        params = {"fit_intercept": [True, False], "normalize": [True, False]}

        # Instanciation et exécution
        search = GridSearchCV(modele, param_grid=params, cv=5, scoring=scorer)
        search.fit(X_train, y_train)

        # Récupération des sorties
        reg = search.best_estimator_  # meilleur modèle

    else:
    # Si les hyper-paramètres ont été défini par l'utilisateur
        # Instanciation du modèle
        reg = LinearRegression(fit_intercept=intercept, normalize=normal)
        # Entrainement
        reg.fit(X_train, y_train)

    # Prediction
    y_pred = reg.predict(X_test)
        # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    # rmse = sqrt(mse)
    # r2 = r2_score(y_test, y_pred)
    np_Xtrain = pd.DataFrame(X_train).to_numpy()

    graph = {'X_1': X_test[:,0], 'Y': y_test, 'Y_pred': y_pred}

    # Pour le graphique:
    # import matplotlib.pyplot as plt
    # plt.plot(y_test, y_pred, ".", color="blue")  # modele predit
    # plt.plot(y_test, y_test, ".", color="green")  # modele réelle
    # plt.show()

    done = time() # fin du chrono
    elapsed = done - start # temps de calcul

    return reg.get_params(), mse, graph, elapsed

# TEST
# import pandas as pd
# bike = pd.read_csv("C:/Users/Axelle/Desktop/M/03_SISE/02_MACHINE LEARNING PYTHON/SEANCE_5/hourly_bike_sharing.csv", sep = ",", encoding = "latin-1", header = 0)
# bike = bike.drop(["dteday", "yr", "temp", "casual", "weekday", "registered"], axis=1)
# recodage_saison = {1: "springer", 2: "summer", 3: "fall", 4: "winter"}
# bike["season"] = bike["season"].map(recodage_saison)
# recodage_weathersit = {1: "clear", 2: "cloudy", 3: "ligh-scnom-rain", 4: "snow-rain"}
# bike["weathersit"] = bike["weathersit"].map(recodage_weathersit)
# bike["mnth"] = bike["mnth"].astype(str)
# bike["hr"] =bike["hr"].astype(str)
# bike2 = pd.get_dummies(bike)
#
# y_bis = bike2["cnt"] #ce que l'utilisateur a défini comme var_cible
# X_bis = bike2.drop("cnt", axis=1)
#
# print(regression_lin(X_bis, y_bis, True)) #test OK
# print(regression_lin(X_bis, y_bis, False, True, True)) #test OK

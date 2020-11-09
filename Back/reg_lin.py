from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt


def regression_lin(X, y, Auto, t_size=None):
    # X = variables explicatives
    # y = variable cible
    # t_size = hyperparametre defini par l'utilisateur permettant de definir la proportion du train/test
    # default = 0.3
    if Auto:
        t_size = 0.3
    # Test de vérification du paramètre t_size
    if t_size < 0 or t_size > 1:
        return "t_size doit être compris entre 0 et 1"

    # Echantillonage
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_size)
    # Instanciation du modèle
    modele = LinearRegression()  # pas d'hyperparametres
    # Entrainement
    modele.fit(X_train, y_train)
    # Prediction
    y_pred = modele.predict(X_test)
    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    rmse = sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # Pour le graphique:
    # import matplotlib.pyplot as plt
    # plt.plot(y_test, y_pred, ".", color="blue")  # modele predit
    # plt.plot(y_test, y_test, ".", color="green")  # modele réelle
    # plt.show()

    return y_pred, mse, rmse, r2

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

# y_bis = bike2["cnt"] #ce que l'utilisateur a défini comme var_cible
# X_bis = bike2.drop("cnt", axis=1)

# print(regression_lin(X_bis, y_bis, 0.35)) #test OK
# print(regression_lin(X_bis, y_bis, 5)) #test OK

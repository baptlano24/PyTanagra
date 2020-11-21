from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from time import time
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer

def regression_lin(X, y, Auto, intercept = True, normal = False):
    # X = features
    # y = target

    start = time()  # starting time

    # Splitting the samples
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Automatic mode --> Optimisation of the parameters
    if Auto:
        # Creation of the model
        scorer = make_scorer(mean_squared_error)
        modele = LinearRegression()
        params = {"fit_intercept": [True, False], "normalize": [True, False]}

        # Cross-Validation
        search = GridSearchCV(modele, param_grid=params, cv=5, scoring=scorer)
        search.fit(X_train, y_train)

        # Outputs
        reg = search.best_estimator_  # best model

    else:
    # If Auto=False, the user chooses the parameters
    #Creation of the model
    reg = LinearRegression(fit_intercept=intercept, normalize=normal)
    reg.fit(X_train, y_train)

    # Prediction
    y_pred = reg.predict(X_test)

    # Evaluation
    mse = mean_squared_error(y_test, y_pred)

    graph = {'X_1': X_test[:,0], 'Y': y_test, 'Y_pred': y_pred}

    done = time() # ending
    elapsed = done - start # computation time

    return reg.get_params(), mse, graph, elapsed

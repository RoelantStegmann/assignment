import numpy as np
import sklearn.metrics


def mse(y, yhat):
    """ Mean Square error """
    return np.mean((y - yhat)**2)


def rmse(y, yhat):
    """ Root Mean Square error """
    return np.sqrt(np.mean(np.square(y - yhat)))


def mae(y, yhat):
    """ Mean Absolute Error """
    return np.mean(y - yhat)


# Just import the AUC
auc = sklearn.metrics.auc
"""
Author: Claire Baxter
Date: 05/07/2021
Description: Module containing a custom BaseEstimator class that can switch between classifiers so that we can setup a
pipeline that uses different classifiers with different sets of hyperparameters

Adapted from: https://stackoverflow.com/a/53926103

Possible future expansions:
"""

from sklearn.base import BaseEstimator
from sklearn.linear_model import SGDClassifier


class ClfSwitcher(BaseEstimator):

    def __init__(self, estimator=SGDClassifier()):
        """
        A Custom BaseEstimator that can switch between classifiers.

        Args:
            estimator: sklearn object - The classifier
        """
        self.estimator = estimator

    def fit(self, X, y=None, **kwargs):
        self.estimator.fit(X, y)
        return self

    def predict(self, X, y=None):
        return self.estimator.predict(X)

    def predict_proba(self, X):
        return self.estimator.predict_proba(X)

    def score(self, X, y):
        return self.estimator.score(X, y)

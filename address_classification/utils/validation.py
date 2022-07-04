"""
Author: Claire Baxter
Date: 04/07/2021
Description: Module containing functionality validating the results

Possible future expansions:
"""

import pandas as pd


def accuracy(df: pd.DataFrame, label_col: str, prediction_col: str) -> pd.DataFrame:
    """
    Function to calculate the accuracy for each classification (country)

    Args:
        df (pd.DataFrame): Pandas dataframe containing the true label and the predicted classification
        label_col (str): Name of the true label column
        prediction_col (str): Name of the prediction column

    Returns:
        df (pd.DataFrame): Grouped pandas dataframe containing the accuracy for each class, as well as the number of
        total entries per class and the number of correctly labelled entries per class
    """

    # A column of correctly labelled
    df['correct'] = df[label_col] == df[prediction_col]

    # Count number of corrects for each classification
    results = df.groupby(label_col).agg(correct=('correct', 'sum'), total=('correct', 'count')).reset_index()
    results['accuracy'] = results['correct'] / results['total']

    return results

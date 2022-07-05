"""
Author: Claire Baxter
Date: 04/07/2021
Description: Module containing functionality preprocessing the data

Possible future expansions:
- Fill missing information
- Parse special characters to roman alphabet
"""

import pandas as pd
import string


def clean_strings(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Function to remove punctuation from strings and convert to lowercase

    Args:
        df (pandas.DataFrame): Dataframe containing col that we want to clean
        col (str): Name of the column that we want to clean

    Returns:
        df (pandas.DataFrame): Cleaned dataframe
    """

    # Convert to lowercase
    df[col] = df[col].str.lower()

    # Remove punctuation
    df[col] = df[col].str.replace('[{}]'.format(string.punctuation), '', regex=True)

    return df

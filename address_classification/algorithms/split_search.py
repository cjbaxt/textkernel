"""
Author: Claire Baxter
Date: 04/07/2021
Description: Module containing brute force city look-up algorithm

Possible future expansions:
- Parallelize the for loops
"""
import collections
import numpy as np
import pandas as pd
from utils import validation


class SplitSearch(object):

    def __init__(self, df: pd.DataFrame, df_ref: pd.DataFrame, add_col: str = 'address',
                 pred_cntry_col: str = 'country_pred', city_col: str = 'city', cntry_col: str = 'country'):
        """
        Initialises Model with the following attributes.

        Args:
            df (pd.DataFrame): Pandas dataframe containing addresses
            df_ref (pd.DataFrame): Pandas dataframe containing cities and corresponding countries
            add_col (str): Name of the address column in df
            pred_cntry_col (str): Name of the output predicted address column after running the algorithm
            city_col (str): Name of the city column in the reference dataset
            cntry_col (str): name of the country column in the reference dataset
            dupe_cities (collections.defaultdict): Default dictionary of cities that occur in multiple countries
        """

        self.df = df
        self.add_col = add_col
        self.pred_cntry_col = pred_cntry_col
        self.df_ref = df_ref
        self.city_col = city_col
        self.cntry_col = cntry_col
        self.dupe_cities = collections.defaultdict(list)

    @staticmethod
    def split_strings(self, col):
        """
        Function to split the string into a list of tokens

        Args:
            self
            col (str): Column of dataframe that we want to split into tokens

        Returns:
            None
        """
        self.df[col] = self.df[col].str.split()

    def run(self):

        # Split the strings of the address column
        self.split_strings(self, self.add_col)

        # Loop over each address
        for i, row in self.df.iterrows():
            # Loop over each token in the address and check if it's in the cities dataframe
            for token in row[self.add_col]:
                if token.isnumeric():
                    pass # Cities are not going to be numeric, we can pass on these

                elif token in self.df_ref[self.city_col].values:
                    try:
                        self.df.loc[i, self.pred_cntry_col] = self.df_ref.loc[
                            self.df_ref[self.city_col] == token, self.cntry_col].item()
                    except ValueError as e:
                        self.dupe_cities[token].append(
                            self.df_ref.loc[self.df_ref[self.city_col] == token, self.cntry_col].values)

    def get_dupe_cities(self):
        """
        Function to return the list of cities which occur in more than one country

        Returns:
            dict: Dictionary of the cities that occur in multiple countries
                keys (str): Cities
                values (list): Countries that the city is in
        """
        for k, l in self.dupe_cities.items():
            self.dupe_cities[k] = list(set(np.array(l).flatten()))

        # Return as normal dictionary
        return dict(self.dupe_cities)

    def get_accuracy(self):
        """
        Function to return the pandas dataframe of accuracy for each class
        """
        acc_df = validation.class_accuracy(self.df, label_col=self.cntry_col, prediction_col=self.pred_cntry_col)

        return acc_df

    def get_df(self):
        """
        Function to return the dataset dataframe
        """
        return self.df

"""
Author: Claire Baxter
Date: 06/07/2021
Description: Module to load an address (or set of addresses) and predict the country
"""

import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from utils import accessors, preprocess
import sys
from tabulate import tabulate

def run(config):

    # Load the model from disk
    loaded_model = pickle.load(open(config['model_filename'], 'rb'))

    # Load the label encoder from disk
    encoder = LabelEncoder()
    encoder.classes_ = np.load(config['encoder_filename'], allow_pickle = True)

    # Load the addresses (convert to df)
    with open(config['address_filename']) as f:
        address = [line.rstrip() for line in f]
    add_df = pd.DataFrame(address, columns=['address'])

    # Preprocess the addresses
    add_df = preprocess.clean_strings(add_df, 'address')

    # Predict the country
    pred_y = encoder.inverse_transform(loaded_model.predict(add_df['address']))
    add_df['country_predict'] = pred_y

    # Return the prediction
    print(tabulate(add_df, headers='keys', tablefmt='psql'))
    add_df.to_csv(config['predict_out_filename'])
    print('Done!')

if __name__ == "__main__":
    # Load config
    config = accessors.get_config(sys.argv[1])

    # Run the creation of the feature
    run(config)
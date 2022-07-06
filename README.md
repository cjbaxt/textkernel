# textkernel
Textkernel programming challenge July 2022.

Create an algorithm for identifying the country an address belongs to.

## Clone repo and set-up the venv 

In order to clone the git repo:

```git clone https://github.com/cjbaxt/textkernel.git```

Make a virtual environment. I chose to make my virtual environment outside the package (on macOS*):

```python3 -m venv <pathname>``` e.g. python3 -m venv ~claire.baxter/virtualenvs/tk_venv  
```source <pathname>/bin/activate```

Then cd to textkernel and install from the requirements.txt:  
```cd textkernel```  
```pip install -r requirements.txt```  

Then cd to address_classification and setup custom modules:  
```cd address_classification```  
```pip install -e .```  
```python import_test.py```

If there are no errors then it works. Now you should be good to go.

*instructions for setting up virtual environments on windows can be found online

## Project structure 
```
|-- README.md
|-- address_classification
|   |-- address_classification.ipynb
|   |-- algorithms
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |-- sklearn_base_estimator.py
|   |   `-- split_search.py
|   |-- config.yml
|   |-- dataset
|   |   |-- LICENSE.txt
|   |   |-- README.md
|   |   |-- addresses.jsonl
|   |   |-- cities.jsonl
|   |   `-- new_addresses.csv
|   |-- import_test.py
|   |-- outputs
|   |   |-- dupe_cities.npy
|   |   |-- encoded_classes.npy
|   |   |-- finalized_model.sav
|   |   |-- split_search_accuracy.csv
|   |   `-- split_search_results.csv
|   |-- predict_country.py
|   |-- setup.py
|   `-- utils
|       |-- __init__.py
|       |-- __pycache__
|       |-- accessors.py
|       |-- preprocess.py
|       `-- validation.py
`-- requirements.txt
```

## To run the code 

I have created a model that can be used to predict country based on incomplete address information. I have broken this 
down into two main files:

### address_classification.ipynb
A notebook containing my approach to the problem and model generation.
This can be opened in jupyter with the following:   
`jupyter notebook address_classification.ipynb`
### predict_country.py
A script to load the model, apply it to new data to get a prediction. 
This can be run with the following:   
```python predict_country.py config.yml```  

 In the config you can specify: 
```
model_filename: path and filename to the exported model
encoder_filename:  path and filename to the label encoder
address_filename: path and filename to a file containing new addresses for classifying, each address separated with a 
new line
predict_out_filename: path and file name to store the outputs
```

Note: The model is limited to and can only classify addresses in the countries that are in the original training set. 

## General approach 

The general approach can be found in my notebook `address_classification.ipynb`. Essentially:
- Load data (see `utils/accessors.py`)
- Calculate some basic statistics on data
  - Any missing data?
  - How many entries?
  - Entries per country? (any countries that are lacking data?)
- Perform any pre-processing (see `utils/preprocess.py`)
  - everything to lowercase
  - remove punctuation 
  - drop duplicates
- A quick implementation of the 'search split' (see `algorithms/search_split.py`). This is the approach described in the assignment guidelines 
  - This achieves around 90% accuracy and has several drawbacks outlined in the notebook. (see `utils/validation.py`)
- I follow this up with a simple machine learning approach:
  - Train test split of dataset 80/20
  - Enocde the label column to numerical values
  - Create a sci-kit learn pipeline to test a couple of different classification models and tune the hyperparameters
    (see `algorithms/sklearn_base_estimator.py`)
- Results  
  - The best model is a Naive Bayes classifer (score = accuracy), achieving 99.7% accuracy on the test data. For the scope of this
  assignment, I deemed this to be an acceptable accuracy score. :) 
  - Export the model to be used in `predict_country.py`
  - Take a look at the incorrectly classified addresses and notice that the algorithm can correctly identify the type 
  of language, e.g. BE is incorrectly identified at FR and NL most of the time.
  
Then one can use `python predict_country.py config.yml` to predict on new data.


## Future improvements
- To scale more this could easily be implemented using Dask instead of pandas or PySpark etc
- Try other word vectorizers, e.g. CountVectorizer, Word2vec
- Take a close look at the behaviour of special characters
- Other classifiers or deep learning models
- On top of these things, several of the files mentioned have some future improvements mentioned in the docstrings

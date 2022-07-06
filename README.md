# textkernel
Textkernel programming challenge July 2022

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

## To run the code 

I have created a model that can be used to predict country based on incomplete address information.   

In `address_classification.ipynb` you will find my working out. This includes: loading the data, preprocessing it, 
quick data analytics, simple model fitting (search city in index) and a machine learning approach where I have tested 
different models and hyperparamter combinations to export the best model (highest accuracy). 

In `predict_country.py` you will find a script to load the model and apply it to new data to get a prediction. New data
can be added to a csv with each new line indicating a new (partial) address, and the location and name of this csv can 
be added to `config.yml`. To run the code simply do:   
```python predict_country.py config.yml```

Note: The model is limited to and can only classify addresses in the countries that are in the original training set. 

## TODO 
fill out the rest of the file

## Initial approach 
- load data 
- calculate some basic statistics on data
  - any missing data?
  - how many entries?
  - how many countries? (e.g. how many classes)
  - entries per country? (any countries that are lacking data?)
- Keep it simple at first
- Perform any pre-processing (if required)
- Train test split of dataset 80/20
- Use sci-kit learn pipelines to test different classification models (but they use tensor flow)


## How to improve in the future
- To scale it this could easily be implemented using Dask instead of pandas, PySpark etc


Figure out how to download the virtual environment so they can run my code 

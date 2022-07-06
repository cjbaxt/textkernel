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

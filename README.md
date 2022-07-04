# textkernel
Textkernel programming challenge July 2022

# Initial approach 
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


# How to improve in the future
- To scale it this could easily be implemented using Dask instead of pandas, PySpark etc

# TODO
Figure out how to download the virtual environment so they can run my code 

import pandas as pd
# import numpy as np

# create a new dataframe 
df = pd.read_csv('Titanic-Dataset.csv')
# information about our dataset
info = df.info()
# columns for our dataset
titles = df.head()

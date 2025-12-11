import pandas as pd
# import numpy as np

# create a new dataframe 
df = pd.read_csv('Titanic-Dataset.csv')
# information about our dataset
info = df.info()
# columns for our dataset
titles = df.head()

print("checking for duplicates\n\n")

duplicates = df.duplicated()
print(duplicates)


print("identifying column Data types")
category_columns = [col for col in df.columns if df[col].dtype == 'object']
numerical_columns  = [col for col in df.columns if df[col].dtypes != 'object']

print('Categorical clolumns: ', category_columns)
print('Numerical columns: ', numerical_columns)


print('Identifying unique values in Columns\n\n\n')


unique_values = df[category_columns].nunique()
print(unique_values)

print("Calculate missing Values as Percentage")
missing_values_percentage  = round((df.isnull().sum() / df.shape[0]) * 100, 2)
print(missing_values_percentage)
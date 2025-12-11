import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

print("Drop Irrelevant or Data-Heavy Missing Columns")
df1 = df.drop(columns=['Name', 'Ticket', 'Cabin'])
df1.dropna(subset=['Embarked'], inplace=True)
df1['Age'].fillna(df1['Age'].mean(), inplace=True)
print(df1)

# detect outliers with Box Plot

# plt.boxplot(df1['Age'], vert=False)
# plt.ylabel('Variable')
# plt.xlabel('Age')
# plt.title('Box Plot')
# plt.show()

# calculate Outlier Boundaries and REmove them
print("Outlier Boundaries and REmove them")
mean = df1['Age'].mean()
std= df1['Age'].std()

lower_bound = mean -2 * std
upper_bound = mean + 2 * std

df2 = df1[(df1['Age']>= lower_bound) & (df1['Age'] <= upper_bound)]

print(df2)

# plt.boxplot(df2['Age'], vert=False)
# plt.ylabel('Variable')
# plt.xlabel('Age')
# plt.title('Box Plot')
# plt.show()

# Impute Missing Data Again
print("Impute Missing Data Again")
df3 = df2.fillna(df2['Age'].mean())
df3.isnull().sum()
print(df3)

mean = df3['Age'].mean()
std = df3['Age'].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

print('Lower Bound :', lower_bound)
print('Upper Bound :', upper_bound)

df4 = df3[(df3['Age'] >= lower_bound) & (df3['Age'] <= upper_bound)]
print(df4)
print("Data validation")
X = df3[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
Y = df3['Survived']


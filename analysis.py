import pandas as pd 
dataframe = pd.read_csv('datasets/diabetic_data.csv')
print(dataframe.head())

#Checking for missing values in dataset
#In the dataset missing values are represented as '?' sign
for col in dataframe.columns:
    if dataframe[col].dtype == object:
         print(col,dataframe[col][dataframe[col] == '?'].count())
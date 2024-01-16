# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
dataframe = pd.read_csv('datasets/diabetic_data.csv')
# Display summary statistics of numerical features
print(dataframe.describe())

# Check for missing values
print(dataframe.isnull().sum())
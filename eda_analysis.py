import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
orders = pd.read_csv('olist_orders_dataset.csv')

# Display first few rows
print("First 5 rows of data:")
print(orders.head())

# Basic info about dataset
print("\nDataset Info:")
print(orders.info())

# Statistical summary
print("\nStatistical Summary:")
print(orders.describe())

# Check for missing values
print("\nMissing Values:")
print(orders.isnull().sum())
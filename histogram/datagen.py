import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Setting random seed for reproducibility
np.random.seed(42)

# Helper functions
def random_date(start, end):
    """Generate a random date between start and end dates."""
    return start + timedelta(days=random.randint(0, (end - start).days))

# Constants for synthetic data generation
num_rows = 5000
customer_ids = [f"CUST_{i:04d}" for i in range(1, num_rows + 1)]
product_ids = [f"PROD_{i:03d}" for i in range(1, 101)]
categories = ['Electronics', 'Clothing', 'Groceries', 'Home Decor', 'Beauty']

# Generating the synthetic dataset
data = {
    'Customer_ID': np.random.choice(customer_ids, num_rows),
    'Age': np.random.randint(18, 80, num_rows),  # Normally distributed ages with a broader range
    'Gender': np.random.choice(['Male', 'Female'], num_rows),
    'Category': np.random.choice(categories, num_rows),
    'Units_Sold': np.random.randint(1, 50, num_rows),  # Distribution with outliers
    'Price_per_Unit': np.round(np.random.uniform(5, 500, num_rows), 2),
    'Total_Sales_Amount': np.nan,  # To be filled with calculated values
    'Product_Rating': np.round(np.random.normal(3.5, 1.0, num_rows), 1),  # Normally distributed ratings
    'Customer_Satisfaction_Score': np.random.choice([1, 2, 3, 4, 5], num_rows, p=[0.1, 0.2, 0.3, 0.2, 0.2]),
    'Purchase_Amount': np.round(np.random.exponential(scale=100, size=num_rows), 2),  # Skewed distribution
    'Noise_Column_1': np.random.choice(['X', 'Y', 'Z'], num_rows),  # Noise data
    'Noise_Column_2': np.random.randint(50, 100, num_rows)  # Noise data
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate Total Sales Amount (Units_Sold * Price_per_Unit)
df['Total_Sales_Amount'] = df['Units_Sold'] * df['Price_per_Unit']

# Introduce missing values in 'Total_Sales_Amount' and 'Purchase_Amount'
nan_indices = np.random.choice(df.index, size=int(num_rows * 0.05), replace=False)
df.loc[nan_indices, 'Total_Sales_Amount'] = np.nan
df.loc[nan_indices, 'Purchase_Amount'] = np.nan

# Introduce some outliers in 'Units_Sold'
outlier_indices = np.random.choice(df.index, size=int(num_rows * 0.01), replace=False)
df.loc[outlier_indices, 'Units_Sold'] = df['Units_Sold'] * 5

# Save the synthetic data to a CSV file (optional)
df.to_csv('synthetic_histogram_data.csv', index=False)

# Display the first few rows of the generated DataFrame
print(df.head())

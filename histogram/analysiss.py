import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Analysis():
    # def __init__():
    #     pass

    def check(self, df:pd.DataFrame):
        nulll = df.isna().sum()
        dtypes = df.dtypes

        # global numeric_columns
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
        # print(numeric_columns)

        #histograms for each numeric column
        for col in numeric_columns:
            # plt.figure(figsize=(8, 5))
            plt.hist(df[col].dropna(), bins=30, edgecolor='black', color='skyblue')
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()

        # print(nulll)
        # print(dtypes)

        # print(len(df.columns))

    def detect_outliers(self, df: pd.DataFrame, column: str):
        plt.figure(figsize=(14, 6))
        # histogram
        plt.subplot(1, 2, 1)
        plt.hist(df[column].dropna(), bins=30, edgecolor='black', color='skyblue')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')

        # Boxplot for Outliers
        plt.subplot(1, 2, 2)
        sns.boxplot(data=df, x=column, color='orange')
        plt.title(f'Boxplot of {column}')
        
        plt.show()

    # Step 2: Measure Outliers' Impact (based on IQR)
    def measure_outliers_impact(self, df: pd.DataFrame, column: str):
        # Calculate quartiles and IQR
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        # Calculate outliers based on 1.5 * IQR rule
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        num_outliers = len(outliers)
        print(f"data type of outliers {outliers.dtypes}")
        
        print(f'Outliers in {column}:')
        print(f'Lower Bound: {lower_bound}, Upper Bound: {upper_bound}')
        print(f'Number of Outliers: {num_outliers}\n')
        
        # Show summary statistics before handling outliers
        print(f"Summary Statistics Before Handling Outliers for {column}:\n")
        print(df[column].describe())
        
        return lower_bound, upper_bound, outliers

    # Step 3: Handle Outliers by Capping or Removing
    def handle_outliers(self, df: pd.DataFrame, column: str, lower_bound, upper_bound):
        
        df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
        df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
        
        
        print(f"Summary Statistics After Handling Outliers for {column}:\n")
        print(df[column].describe())

    # Step 4: Handle Missing Data by Imputing
    def handle_missing_data(self, df: pd.DataFrame, column: str):
        # Fill missing values with median 
        median_value = df[column].median()
        df[column].fillna(median_value, inplace=True)
        
        print(f"Missing data in {column} handled by imputing with the median value: {median_value}")
        print(df[column].isna().sum(), "missing values remaining in", column)

    # Step 5: Compare Before and After Handling
    def compare_before_after(self, original_df: pd.DataFrame, modified_df: pd.DataFrame, column: str):
        print(f"Comparison for {column} Before and After Handling Outliers:\n")
        
        
        print("Before:\n", original_df[column].describe())
        
        
        print("\nAfter:\n", modified_df[column].describe())





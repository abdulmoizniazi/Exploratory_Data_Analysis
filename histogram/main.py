import pandas as pd
from histogram.analysiss import Analysis

df = pd.read_csv('synthetic_histogram_data.csv')
# df = pd.DataFrame(data)
print(df.head())
# df.to_pickle('data.pkl')

ana = Analysis()
ana.check(df)
ana.detect_outliers(df, "Units_Sold")
ana.measure_outliers_impact(df, "Units_Sold")
lower, upper, outlier = ana.measure_outliers_impact(df, "Units_Sold")
ana.handle_outliers(df, "Units_Sold", lower, upper)
ana.handle_missing_data(df, "Units_Sold")
ana.compare_before_after(df, "Units_Sold")

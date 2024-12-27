import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv("python/data_analysis/daily-activities/Daily-activity-metrics.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Group by Month, sum Heart Points, and sort by calendar order
heartpoints_summary = (
    df.groupby('Month', sort=False)['Heart Points']
    .sum()
    .reindex(month_order)
    .dropna()
    .reset_index()
)
heartpoints_summary.columns = ['Month', 'Total Heart Points']

print(heartpoints_summary)
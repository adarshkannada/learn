import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv("python/data_analysis/daily-activities/Daily-activity-metrics.csv")
# print(df.dtypes)
df['Date'] = pd.to_datetime(df['Date'])
# print(df.dtypes)

df['MonthName'] = df['Date'].dt.strftime('%B')
monthly_heart_points = df.groupby('MonthName')['Heart Points'].sum()
print(monthly_heart_points)
df_monthly = pd.DataFrame(list(monthly_heart_points.items()), columns=['MonthName', 'HeartPoints'])
# df_monthly['MonthName'] = pd.Categorical(df_monthly['MonthName'], categories=df['MonthName'], ordered=True)
print(df_monthly)

x = df_monthly['MonthName'].tolist()
y = df_monthly['HeartPoints'].tolist()

plt.plot(x, y)
plt.xlabel('MonthName')
plt.ylabel('HeartPoints')
plt.title('2024-heartpoints-earned')
# plt.savefig("fileout.jpg")
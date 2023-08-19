import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('./covid_19_india.csv')
df2 = pd.read_csv('./StatewiseTestingDetails.csv')

# print(df1)
# print(df2)

# print(df1.info())
# print(df2.info())

df1.rename(columns = {"State/UnionTerritory": "State"}, inplace = True)
# print(df1.head())
duplicate_list = []
for state in df1['State'].unique().tolist():
    total = df2[df2['State'] == state]['State'].count()
    if total > 0:
        duplicate_list.append(state)

df2.fillna(0, inplace = True)

data1 = df1[df1['State'].isin(duplicate_list)]
data1 = data1[(data1['Date'] >= '2020-04-17') & (data1['Date'] <= '2021-08-10')]
print(data1)
data2 = df2[df2['State'].isin(duplicate_list)]


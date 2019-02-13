import pandas as pd
import numpy as np
import matplotlib as plt
plt.use('TkAgg')
import seaborn as sns

# import the csv file as a pandas data frame
# file requires pre-processing outside python
rain_data = pd.DataFrame(pd.read_csv('rain_data.csv'))

# look at the data frame
# print(rain_data)
# print(rain_data.dtypes)
# print(rain_data.columns)


# deal with missing data
rain_data.replace('', np.nan)
# print(rain_data)
# print(rain_data[rain_data.h0 == '-'])

rain_data['Total'].apply(pd.to_numeric)
rain_data['Date'] = pd.to_datetime(rain_data['Date'], format = '%m/%d/%y')
print(rain_data.dtypes)
print(rain_data)

g = sns.regplot(x='Date', y='Total', kind='line', data=rain_data)
g.fig.autofmt_xdate()
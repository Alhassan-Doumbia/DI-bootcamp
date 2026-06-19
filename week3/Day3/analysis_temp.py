import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, shapiro

path = 'AAPL_1981_2023.csv'
print('path exists', __import__('os').path.exists(path))
stocks_data = pd.read_csv(path)
print('shape', stocks_data.shape)
print(stocks_data.head().to_string())
missing = stocks_data.isnull().sum()
print('missing per column:\n' + missing.to_string())
print('any missing', missing.any())
print('\ncolumn types:')
for column in stocks_data.columns:
    print(column, stocks_data[column].dtype)
print('\nsummary describe:')
print(stocks_data.describe().to_string())

stocks_data['Date'] = pd.to_datetime(stocks_data['Date'], format='%d/%m/%Y')
print('date range', stocks_data['Date'].min(), stocks_data['Date'].max())

stocks_data['Year'] = stocks_data['Date'].dt.year
close_1981 = stocks_data[stocks_data['Year']==1981]['Close']
close_1982 = stocks_data[stocks_data['Year']==1982]['Close']
print('len1981', len(close_1981), 'len1982', len(close_1982))
res = ttest_ind(close_1981, close_1982, equal_var=False)
print('ttest stat', res.statistic, 'p', res.pvalue)

stocks_data['Daily_Return'] = stocks_data['Close'].pct_change()
print('daily return head:')
print(stocks_data['Daily_Return'].head().to_string())
returns = stocks_data['Daily_Return'].dropna()
print('returns count', len(returns))
print('returns min/max', returns.min(), returns.max())
print('returns mean/std', returns.mean(), returns.std())
if len(returns) > 500:
    sample = returns.sample(500, random_state=0)
else:
    sample = returns
stat, p = shapiro(sample)
print('shapiro stat', stat, 'p', p)

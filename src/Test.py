import pandas as pd

data = pd.Series([1, 2, 3, 4])

data_range = data.describe()["max"] - data.describe()["min"]
print(data)
print(data ** 2)
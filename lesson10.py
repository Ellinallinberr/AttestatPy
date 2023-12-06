import pandas as pd

# Ваш исходный код
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


unique_values = data['whoAmI'].unique()
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)


data = data.drop('whoAmI', axis=1)

print(data.head())
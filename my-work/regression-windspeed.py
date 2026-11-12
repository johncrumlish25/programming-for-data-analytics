# Check if there is a relation between windspeed and the month at Knock Airport
# Author: John Crumlish

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
datadir = "../data/"
filename = datadir + "mly4935.csv"

df = pd.read_csv(filename, skiprows=19)
print(df.head(5))

# Correlation between month and mean temp
corrtemp = df["month"].corr(df["meant"])
print(corrtemp)

# Keep only month and windspeed
cleandf = df[["month","wdsp"]]

# Drop NAs
cleandf['wdsp'] = cleandf.loc[:,('wdsp')].replace(' ', np.nan)
cleandf.dropna(inplace=True)

cleandf['wdsp'] = cleandf['wdsp'].astype(float)

corrwind = cleandf["month"].corr(cleandf["wdsp"])
print(f"Wind Correlation {corrwind}")

sns.set_style('whitegrid')
sns.lmplot(x='month', y='wdsp', order=3, data=cleandf)
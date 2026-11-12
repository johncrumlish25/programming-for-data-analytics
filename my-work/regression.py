# Regression
# Author: John Crumlish

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
dataset = sns.load_dataset('tips')

sns.set_style('whitegrid')
sns.lmplot(x='size', y='tip', data=dataset, x_estimator=np.mean)

plt.show()
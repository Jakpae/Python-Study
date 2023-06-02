import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Seaborn dataset : ", sns.get_dataset_names())
# load data set as pandas data frame 
df_titanic = sns.load_dataset("titanic")
print("\nSeaborn titanic :\n", df_titanic)
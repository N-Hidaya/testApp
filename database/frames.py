## Determine data types
import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

display(tips.head())

# display types of each column
print(tips.dtypes)

# Stack the dataframes on top of each other
verticall_stacked = pd.concat([df1,df2,df3], axis=0)
display(verticall_stacked)


# Importing pandas library
import pandas as pd
from pathlib import Path

# Load the data of example.csv
# with tab as custom delimiter
# into a Dataframe df
df = pd.read_csv('../input/data.csv',
                 sep=',',
                 engine='python')


# index_col=[1,2,3,4])

# Print the Dataframe


def absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()


print(df.loc[0][1])
print(df)
print(absolutepath('../input/data.csv'))


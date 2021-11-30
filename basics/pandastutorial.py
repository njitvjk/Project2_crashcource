import pandas as pd

# Load the data of example.csv
# with tab as custom delimiter
# into a Dataframe df
df = pd.read_csv('example3.csv',
                 sep='\t',
                 engine='python')

# Print the Dataframe
df
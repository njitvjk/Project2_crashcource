import numpy as np
import pandas as pd


"""Read CSV and convert to dataframe"""
data_set = pd.read_csv("C:\\Users\\thiya\\OneDrive\\Documents\\Sem2\\DataAnalytics\\heart.csv")
print(data_set)
"""Question1:Find the record with the highest trestbps"""
print("the maximum in column trestbps is :",data_set['trestbps'].max())

"""Question2:Find out the oldpeak value for the record index 200"""
print("the oldpeak value for the record index 200 is:",data_set.at[200,'oldpeak'])

"""Question3:Pick out the last 10 records as a small dataset A"""
data_set_A = data_set.tail(10)
print("\nthe last 10 records as a small dataset A:\n",data_set_A)

"""Question4:Within A, add a new column named verified"""
"""Question5:Within A, set all values in column verified as NAN"""
data_set_A.insert(0,'verified',np.NAN)
print(data_set_A)

"""Question6:Within A, update the first record column verified as 1"""
data_set_A.at[293,'verified']='1'
print("\n update the first record column verified as 1:\n",data_set_A)

"""Question7:Within A, remove all NAN rows"""
data_set_A=data_set_A.dropna()
print(" \nAfter removing rows with NAN:\n",data_set_A)

"""Question8:Within A, draw a histogram or a box graph for the dataset."""

data_set_A.plot.hist()





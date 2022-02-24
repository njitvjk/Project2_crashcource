import pandas as pd
import matplotlib as plot
import matplotlib.pyplot

data_set = pd.read_csv("../done/Iris.csv")
x = data_set.loc[:, "PetalLengthCm"]
y = data_set.loc[:, "PetalWidthCm"]

plot.pyplot.scatter(x, y)

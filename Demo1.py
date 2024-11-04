import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# plot a line graph

# xpts=np.array([0,10])
# ypts=np.array([0,20])
# plt.plot(xpts, ypts)

#  data

data={
    "Cricket_Bat":["SG","DGM","SS","GM"],
    "MRP":[2000,2300,2800,3000],
    "Weight_Grass":[1100,1200,1250,1350]
}

# Create a dataFrame

dataFrame=pd.DataFrame(data)

#  Plot a line graph

plt.plot(dataFrame["MRP"],dataFrame["Weight_Grass"])

# The grid

plt.grid()

# The labels

plt.xlabel("Bat Price (MRP)")
plt.ylabel("Bat Weight (Grams)")

# Display the figure

plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data =pd.read_csv('/content/householdtask3.csv')

data.head(10)

#Scatter Plot

plt.scatter(data['year'],data['own'])

#Adding title to the plot

plt.title('Scatter plot')

#Setting x and y lables

plt.xlabel('Year')
plt.ylabel('own')

#Result
plt.show()

#Line chart with year against own

plt.plot(data['year'])
plt.plot(data['own'])

#Adding title

plt.title('Line chart')

#x and y Lables
plt.xlabel('year')
plt.ylabel('own')

#Result
plt.show()

#bar chart 
plt.bar(data['year'],data['own'])
#Adding title

plt.title('Bar Chart')

#x and y Lables
plt.xlabel('year')
plt.ylabel('own')

#Result
plt.show()

#Histogram

plt.hist(data['income'])

plt.title('Histogram')

plt.show()

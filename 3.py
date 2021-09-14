import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a=pd.read_csv('C:/Users/yukti singh/Desktop/iris.csv')
b=np.array(a['sepal length'])
c=np.array(a['petal length'])
d=np.array(a['sepal width'])
e=np.array(a['petal width'])

##121-row column section##



plt.scatter(b,c,color='blue')
plt.scatter(d,e,color='red',marker='*')
plt.title('graph between sepal and petal length and width')
plt.xlabel('sepal ')
plt.ylabel("petal ")


plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

AgeLoan = np.array ([[25,40000],
                        [35,60000],
                        [45,80000],
                        [20,20000],
                        [35,120000],
                        [52,18000],
                        [23,95000],
                        [40,62000],
                        [60,100000],
                        [48,220000],
                        [33,120000]])



Default=np.array(['N','N','N','N','N','N','Y','Y','Y','Y','Y'])

n=KNeighborsClassifier(n_neighbors=3)
trained=n.fit(AgeLoan,Default)
y_pred1=trained.predict([[48,142000]])
print(y_pred1)

plt.scatter(AgeLoan[0:6,0],AgeLoan[0:6,1],marker='*',color='red',label='NO')
plt.scatter(AgeLoan[6:11,0],AgeLoan[6:11,1],marker='^',color='blue',label='YES')
plt.scatter(48,142000,color='green')



plt.title('KNN data')
plt.xlabel('Age')
plt.ylabel('Loan')
plt.legend()
plt.show()

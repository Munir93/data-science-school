import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler


#accessing wine data, formating and setting column headings
#you can download the dataset here http://archive.ics.uci.edu/ml/machine-learning-databases/wine/
df = pd.read_table('C:\\Users\Admin\Downloads\KNNBCdata\wine.data', sep=",", names= ["ClassID","Alcohol",
 "Malic acid",
 "Ash",
 "Alcalinity of ash",
"Magnesium",
"Total phenols",
 "Flavanoids",
 "Nonflavanoid phenols",
"Proanthocyanins",
"Color intensity",
"Hue",
"OD280/OD315 of diluted wines",
"Proline" ])

#suffuling rows
shufDF = df.sample(frac=1)

#scaling object so we can convert data to the same scale for use in the model
scaler  = StandardScaler()

# applyting the scaling fuction to the data set minus the class id (reults column)
scaler.fit(shufDF.drop('ClassID', axis=1))  #sets the scaler to teh data set
scaled_features = scaler.transform(shufDF.drop('ClassID',axis = 1))  # transforms features to scaled version
df_feat = pd.DataFrame(scaled_features,columns=shufDF.columns[1:]) # converts scaled features to dataframe

#train and test generator
from sklearn.model_selection import train_test_split

#70:30 split
x_train,x_test, y_train, y_test = train_test_split(scaled_features,shufDF['ClassID'],test_size=0.3)

#showing first 5 rows to see if they scaled properly
print(df_feat.head())

from sklearn.neighbors import KNeighborsClassifier

#using an initial K value of 1
knn = KNeighborsClassifier(n_neighbors=1)

#training model on the data
knn.fit(x_train,y_train)

#using our trained model to predict reults
pred = knn.predict(x_test)

# confustion matrix asseses how well the model performed
# classification report shows important metrics such as precision - true positives to true positive + fasle positive
#i.e not labeling a sample negative that is positve
from sklearn.metrics import classification_report,confusion_matrix


print(confusion_matrix(y_test,pred))

print(classification_report(y_test,pred))


# here we calculate the mean error for k valvues in range 1 to 30
# and plot results using Matplotlib

error_rate = []

for i in range (1,30):

      knn = KNeighborsClassifier(n_neighbors=i)
      knn.fit(x_train,y_train)
      pred_i = knn.predict(x_test)
      error_rate.append(np.mean(pred_i != y_test))


plt.figure(figsize=(10,6))
plt.plot(range(1,30),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

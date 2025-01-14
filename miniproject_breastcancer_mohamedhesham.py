# -*- coding: utf-8 -*-
"""miniProject_breastCancer_MohamedHesham.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NRPlcdsGTu8XzNg7J67qZrr4K74MlZpW
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score,precision_score
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
import time
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

X, y = load_breast_cancer(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

"""# **Model declarations**"""

kernels = ['linear', 'poly', 'rbf', 'sigmoid']
tree = DecisionTreeClassifier(random_state=0)
randforest = RandomForestClassifier(n_estimators=5, random_state=0)
boosting= GradientBoostingClassifier(random_state=0)
logireg = LogisticRegression(random_state=0)
KNN=KNeighborsClassifier(n_neighbors=3)

"""# **Assigning the coloums**"""

results = pd.DataFrame(columns=['Model', 'Kernel', 'Accuracy', 'Precision', 'Recall', 'Training Time'])
results

"""# **The SVM model**"""

for kernel in kernels:
  svm = SVC(kernel=kernel)
  start_time = time.time()
  svm.fit(x_train, y_train)
  end_time = time.time()
  svm_training_time = end_time - start_time
  svm_y_pred = svm.predict(x_test)
  svm_accuracy = accuracy_score(svm_y_pred, y_test)
  svm_precision = precision_score(y_test, svm_y_pred, average='weighted')
  svm_recall = recall_score(y_test, svm_y_pred, average='weighted')
  results= results.append({'Model': 'SVM', 'Kernel': kernel, 'Accuracy': svm_accuracy, 'Precision': svm_precision, 'Recall': svm_recall, 'TrainingTime': svm_training_time}, ignore_index=True)

"""# **the tree model**"""

start_time = time.time()
tree.fit(x_train, y_train)
end_time = time.time()
tree_training_time = end_time - start_time
tree_y_pred = tree.predict(x_test)
tree_accuracy = accuracy_score(tree_y_pred, y_test)
tree_precision = precision_score(y_test, tree_y_pred, average='weighted')
tree_recall = recall_score(y_test, tree_y_pred, average='weighted')
results= results.append({'Model': 'Decision Tree', 'Accuracy': tree_accuracy, 'Precision': tree_precision, 'Recall': tree_recall, 'Training Time': tree_training_time}, ignore_index=True)

"""# **the random forest model**"""

start_time = time.time()
randforest.fit(x_train, y_train)
end_time = time.time()
randforest_training_time = end_time - start_time
randforest_y_pred = randforest.predict(x_test)
randforest_accuracy = accuracy_score(randforest_y_pred, y_test)
randforest_precision = precision_score(y_test, randforest_y_pred, average='weighted')
randforest_recall = recall_score(y_test, randforest_y_pred, average='weighted')
results= results.append({'Model': 'Random Forest',  'Accuracy': randforest_accuracy, 'Precision': randforest_precision, 'Recall': randforest_recall, 'Training Time': randforest_training_time}, ignore_index=True)

"""# **the boosting model**"""

start_time = time.time()
boosting.fit(x_train, y_train)
end_time = time.time()
boosting_training_time = end_time - start_time
boosting_y_pred = boosting.predict(x_test)
boosting_accuracy = accuracy_score(boosting_y_pred, y_test)
boosting_precision = precision_score(y_test, boosting_y_pred, average='weighted')
boosting_recall = recall_score(y_test, boosting_y_pred, average='weighted')
results= results.append({'Model': 'Gradient Boosting', 'Accuracy': boosting_accuracy, 'Precision': boosting_precision, 'Recall': boosting_recall, 'Training Time': boosting_training_time}, ignore_index=True)

"""# **the logireg model**"""

start_time = time.time()
logireg.fit(x_train, y_train)
end_time = time.time()
logireg_training_time = end_time - start_time
logireg_y_pred = logireg.predict(x_test)
logireg_accuracy = accuracy_score(logireg_y_pred, y_test)
logireg_precision = precision_score(y_test, logireg_y_pred, average='weighted')
logireg_recall = recall_score(y_test, logireg_y_pred, average='weighted')
results= results.append({'Model': 'Logistic Regression', 'Accuracy': logireg_accuracy, 'Precision': logireg_precision, 'Recall': logireg_recall, 'Training Time': logireg_training_time}, ignore_index=True)

"""# **The KNN model**"""

start_time = time.time()
KNN.fit(x_train,y_train)
end_time = time.time()
KNN_training_time = end_time - start_time
KNN_y_pred=KNN.predict(x_test)
KNN_accuracy = accuracy_score(KNN_y_pred, y_test)
KNN_precision = precision_score(y_test, KNN_y_pred, average='weighted')
KNN_recall = recall_score(y_test, KNN_y_pred, average='weighted')
results= results.append({'Model': 'KNN', 'Accuracy': KNN_accuracy, 'Precision': KNN_precision, 'Recall': KNN_recall, 'Training Time': KNN_training_time}, ignore_index=True)

print(results)
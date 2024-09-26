# -*- coding: utf-8 -*-
"""Financial Risk Assesment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FSAXmFOKzN8KEvzj0bp8e5XrSlu_U1HB
"""
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("financial_risk_assessment.csv")
# df
#
# df.info()
#
# df.head()
#
# df.describe()
#
# df.nunique()
#
# df.isnull().sum()

df = df.drop('Gender', axis=1)

# df.head()

df['Income'] = df['Income'].fillna(df['Income'].median())
df['Credit Score'] = df['Credit Score'].fillna(df['Credit Score'].median())
df['Loan Amount'] = df['Loan Amount'].fillna(df['Loan Amount'].median())
df['Assets Value'] = df['Assets Value'].fillna(df['Assets Value'].median())
df['Number of Dependents'] = df['Number of Dependents'].fillna(df['Number of Dependents'].median())
df['Previous Defaults'] = df['Previous Defaults'].fillna(df['Previous Defaults'].median())

import numpy as np

# Filling missing values with mean for numerical columns
numerical_cols = df.select_dtypes(include=np.number).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

# Filling missing values with mode for categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

# Checking if any missing values remain
# df.isnull().sum()

duplicates = df.duplicated()
print("Number of duplicate rows:", duplicates.sum())
df_no_duplicates = df.drop_duplicates()

# df.dtypes

numerical_columns = ['Income', 'Credit Score', 'Loan Amount', 'Debt-to-Income Ratio', 'Assets Value',
                     'Years at Current Job', 'Previous Defaults']

# plt.figure(figsize=(14, 10))

# for i, col in enumerate(numerical_columns, 1):
#     plt.subplot(3, 3, i)
#     df.boxplot(column=[col])
#     plt.title(f'Boxplot of {col}')

# plt.tight_layout()
# plt.show()

"""EDA"""

import matplotlib.pyplot as plt
# Histograms for numerical features
# df.hist(figsize=(12, 10))
# plt.suptitle('Histograms of Numerical Features', y=1.02)
# plt.tight_layout()
# plt.show()

# numerical_df = df.select_dtypes(include=['number'])
# correlation_matrix = numerical_df.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlation Matrix')
# plt.show()

# categorical_columns = ['Employment Type', 'Education Level', 'Marital Status', 'Has Mortgage', 'Has Dependents', 'Loan Purpose']
# for col in categorical_columns:
#      if col in df.columns:
#         plt.figure(figsize=(8, 6))
#         sns.countplot(x=col, data=df)
#         plt.title(f'Countplot of {col}')
#         plt.xticks(rotation=45, ha='right')
#         plt.tight_layout()
#         plt.show()
#     else:
#         print(f"Warning: Column '{col}' not found in DataFrame.")

# print(df.columns)
# sns.pairplot(df[['Income','Credit Score','Loan Amount','Debt-to-Income Ratio','Risk Rating']],hue='Risk Rating')
# plt.suptitle('Pairplot of Selected Features', y=1.02)
# plt.show()

# for col in numerical_columns:
#     plt.figure()
#     sns.histplot(df[col], kde=True)
#     plt.title(f"Distribution of {col}")
#     plt.xlabel(col)
#     plt.ylabel("Frequency")
#     plt.show()

# categorical_columns = ['Employment Status', 'Education Level', 'Marital Status'] # Removed the duplicate 'Employment Type'
# for col in categorical_columns:
#     plt.figure()
#     sns.countplot(x=df[col])
#     plt.title(f"Count of {col}")
#     plt.xlabel(col)
#     plt.ylabel("Count")
#     plt.xticks(rotation=45, ha='right')
#     plt.show()

# df.head()
#
# boolean_columns = df.select_dtypes(include='bool').columns
# for col in boolean_columns:
#   df[col] = df[col].astype(object)
# print(df.dtypes)

# from sklearn.preprocessing import LabelEncoder
# label_encoder = LabelEncoder()
# categorical_columns = ['Employment Status', 'Education Level', 'Marital Status' ]
# for col in categorical_columns:
#     df[col] = label_encoder.fit_transform(df[col])
#
# df

from sklearn.preprocessing import StandardScaler

numerical_columns = ['Income', 'Credit Score', 'Loan Amount', 'Debt-to-Income Ratio', 'Assets Value',
                     'Years at Current Job', 'Previous Defaults']
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# df

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

X = df.drop('Risk Rating', axis=1)
y = df['Risk Rating']
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)
# print("y_train shape:", y_train.shape)
# print("y_test shape:", y_test.shape)

from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics
from sklearn.model_selection import train_test_split

"""1.RANDOM FOREST"""

rf_classifier = RandomForestClassifier(random_state=42)
object_columns = X_train.select_dtypes(include=['object']).columns
X_train = pd.get_dummies(X_train, columns=object_columns)
X_test = pd.get_dummies(X_test, columns=object_columns)
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)
rf_classifier.fit(X_train, y_train)
y_pred = rf_classifier.predict(X_test)
accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
precision = sklearn.metrics.precision_score(y_test, y_pred)
recall = sklearn.metrics.recall_score(y_test, y_pred)
f1 = sklearn.metrics.f1_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

"""2.LOGISTIC REGRESSION"""

from sklearn.linear_model import LogisticRegression

# logistic_model = LogisticRegression(max_iter=1000, random_state=42)
# logistic_model.fit(X_train, y_train)
# y_pred_logistic = logistic_model.predict(X_test)
# accuracy_logistic = accuracy_score(y_test, y_pred_logistic)
# precision_logistic = precision_score(y_test, y_pred_logistic, average='weighted')
# recall_logistic = recall_score(y_test, y_pred_logistic, average='weighted')
# f1_logistic = f1_score(y_test, y_pred_logistic, average='weighted')

# print("Logistic Regression Metrics:")
# print("Accuracy:", accuracy_logistic)
# print("Precision:", precision_logistic)
# print("Recall:", recall_logistic)
# print("F1-score:", f1_logistic)

"""3.DECISION TREES"""

from sklearn.tree import DecisionTreeClassifier

# dt_classifier = DecisionTreeClassifier(random_state=42)
# dt_classifier.fit(X_train, y_train)
# y_pred_dt = dt_classifier.predict(X_test)
# accuracy_dt = accuracy_score(y_test, y_pred_dt)
# precision_dt = precision_score(y_test, y_pred_dt, average='weighted')
# recall_dt = recall_score(y_test, y_pred_dt, average='weighted')
# f1_dt = f1_score(y_test, y_pred_dt, average='weighted')

# print("Decision Tree Metrics:")
# print("Accuracy:", accuracy_dt)
# print("Precision:", precision_dt)
# print("Recall:", recall_dt)
# print("F1-score:", f1_dt)

"""4.K-NEAREST NEIGHBORS(KNN)"""

from sklearn.neighbors import KNeighborsClassifier
# knn_classifier = KNeighborsClassifier(n_neighbors=5)
# knn_classifier.fit(X_train, y_train)
# y_pred_knn = knn_classifier.predict(X_test)
# accuracy_knn = accuracy_score(y_test, y_pred_knn)
# precision_knn = precision_score(y_test, y_pred_knn, average='weighted')
# recall_knn = recall_score(y_test, y_pred_knn, average='weighted')
# f1_knn = f1_score(y_test, y_pred_knn, average='weighted')

# print("K-Nearest Neighbors Metrics:")
# print("Accuracy:", accuracy_knn)
# print("Precision:", precision_knn)
# print("Recall:", recall_knn)
# print("F1-score:", f1_knn)

from sklearn.model_selection import RandomizedSearchCV

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}
rf_classifier = RandomForestClassifier(random_state=42)
random_search = RandomizedSearchCV(
    estimator=rf_classifier,
    param_distributions=param_grid,
    n_iter=10,
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)
random_search.fit(X_train, y_train)
print("Best parameters:", random_search.best_params_)
print("Best score:", random_search.best_score_)
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
print("Accuracy on test set:", accuracy)

pickle.dump(best_model, open('model.pkl', 'wb'))
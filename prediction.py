import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('price.csv')

"""**Label Encoding the Car Make and dropping Car Model as we don't need it**"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Car Make'] = le.fit_transform(df['Car Make'])

df.drop(columns='Car Model',axis=1,inplace=True)

df['Price (in USD)']=df['Price (in USD)'].str.replace(',', '')
df['Price (in USD)']=df['Price (in USD)'].astype(int)

df['Engine Size (L)'] = pd.to_numeric(df['Engine Size (L)'], errors='coerce')
df['Horsepower'] = pd.to_numeric(df['Horsepower'], errors='coerce')
df['Torque (lb-ft)'] = pd.to_numeric(df['Torque (lb-ft)'], errors='coerce')
#df['Price (in USD)'] = pd.to_numeric(df['Price (in USD)'], errors='coerce')
df['0-60 MPH Time (seconds)'] = pd.to_numeric(df['0-60 MPH Time (seconds)'], errors='coerce')

"""**Filling NaN values with mean of that column**"""

df.fillna(df.mean(skipna=True),inplace=True)

"""**Converting the data type of columns to integer**"""

df['Engine Size (L)']=df['Engine Size (L)'].astype(int)
df['Horsepower']=df['Horsepower'].astype(int)
df['Torque (lb-ft)']=df['Torque (lb-ft)'].astype(int)
df['0-60 MPH Time (seconds)']=df['0-60 MPH Time (seconds)'].astype(int)

"""**Creating a new feature i.e. Age of the car**"""

import datetime
yr = datetime.datetime.now().year

df['Age'] = yr - df['Year']

"""**Linear Regression Algorithm**"""

from sklearn.model_selection import train_test_split
X = df.drop(columns='Price (in USD)',axis=1)

y=df['Price (in USD)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

# Create an instance of the Linear Regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

from sklearn.metrics import r2_score

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate R-squared value
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

"""**Decision Tree Algorithm**"""

from sklearn.tree import DecisionTreeRegressor

tree_model = DecisionTreeRegressor()

# Fit the model to the training data
tree_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred_tree = tree_model.predict(X_test)

X = df[['Engine Size (L)', 'Horsepower', 'Torque (lb-ft)', '0-60 MPH Time (seconds)', 'Age']]
y = df['Price (in USD)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=52)

# Create an instance of the Decision Tree Regressor
dec_model = DecisionTreeRegressor()

# Fit the model to the training data
dec_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dec_model.predict(X_test)
print(y_pred)
# Calculate R-squared value
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

"""**Cross Validation**"""

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Split the data into training and test sets
X = df[['Engine Size (L)', 'Horsepower', 'Torque (lb-ft)', '0-60 MPH Time (seconds)', 'Age']]
y = df['Price (in USD)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid to search
param_grid = {
    'max_depth': [None, 3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': [1.0, 'sqrt', 'log2']
}

# Create an instance of the Decision Tree Regressor
model = DecisionTreeRegressor()

# Perform grid search to find the best hyperparameters
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)

# Get the best model and its hyperparameters
best_model = grid_search.best_estimator_
best_params = grid_search.best_params_

# Make predictions on the test set using the best model
y_pred = best_model.predict(X_test)

# Calculate R-squared value
r2 = r2_score(y_test, y_pred)
print(f"Best Parameters: {best_params}")
print(f"R-squared: {r2}")

tree_r2 = r2_score(y_test,y_pred_tree)

print(f"R-squared: {r2}")

X.head(1)

y

dec_model.predict([[3,379,331,4,1]])

"""**Decision Tree algorithm has a way better accuracy than linear regression for the above problem**"""

import pickle
pickle.dump(dec_model, open('model33.pkl', 'wb'))

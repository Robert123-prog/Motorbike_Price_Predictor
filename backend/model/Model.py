import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset
dataset = pd.read_csv('BIKE DETAILS.csv')

# Extract features and target
X = dataset[['name', 'year', 'seller_type', 'owner', 'km_driven', 'ex_showroom_price']]
y = dataset['selling_price']

# Impute missing values using mean strategy for 'km_driven' and 'ex_showroom_price'
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Apply the imputer safely using .loc to avoid SettingWithCopyWarning
X.loc[:, ['km_driven', 'ex_showroom_price']] = imputer.fit_transform(X[['km_driven', 'ex_showroom_price']])

# Ceil the imputed values
X.loc[:, ['km_driven', 'ex_showroom_price']] = np.ceil(X[['km_driven', 'ex_showroom_price']])

# Encode categorical columns and pass through numerical columns
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), ['name', 'seller_type', 'owner'])], remainder='passthrough')

# Apply the transformer to X
X = ct.fit_transform(X)

# Convert target to numpy array
y = y.values

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict test set results
y_pred = regressor.predict(X_test)

# Set precision for printing results
np.set_printoptions(precision=2)

# Print predictions alongside actual values
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Save the trained model and preprocessor for later use
# joblib.dump(regressor, "trained_model.pkl")
# joblib.dump(ct, "preprocessor.pkl")

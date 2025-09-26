# ---Can you predict house price based on the number of rooms and location?---

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# ---Load----
df = pd.read_csv(r"C:\Users\pc20\Downloads\Housing.csv")
print(df.head())
print(df.info())

# ---check for null values---
print(df.isnull().sum())
df = df.dropna()
print(df.isnull())


# ---Preprocess---

x = df[['area', 'bedrooms', 'mainroad', 'basement', 'parking']]
y = df[['price']]

x = pd.get_dummies(x, columns=['mainroad','basement'], drop_first=True)
print(x.head())

# ---train---

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

# ---predict---
y_pred = model.predict(x_test)


# ---evaluate---
print("R^2 Score:", r2_score(y_test, y_pred))

# Example prediction
example = pd.DataFrame(columns=x.columns)
example.loc[0] = [2500, 4, 1, 0, 2]  

predicted_price = model.predict(example)
predicted_value = predicted_price.item()
print(f"Predicted Price for the house: ${predicted_value:,.2f}")
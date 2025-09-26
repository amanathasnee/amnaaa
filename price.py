import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([500,800,1000,1200,1500]).reshape(-1,1) #reshape is to convert 1D to 2D
y=np.array([150000,200000,230000,260000,300000])

model=LinearRegression()
model.fit(x,y)

print("intercept(base price) : ",model.intercept_)
print("slope (price per sqft) : ",model.coef_[0])

size=1100
pred_price = model.predict([[size]])
print(f"predicted price for {size} sqrt = $ {pred_price[0] : .2f}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# load dataset
df = pd.read_csv(r"C:\Users\pc20\Downloads\student_exam_scores.csv")
print(df.head())
print(df.isnull().sum())

# features and target
X = df[["hours_studied"]]   # feature (2D DataFrame)
y = df["exam_score"]        # target (Series)

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# predictions
y_pred = model.predict(X_test)

# evaluation

r2 = r2_score(y_test, y_pred)

print("R2 Score:", r2)

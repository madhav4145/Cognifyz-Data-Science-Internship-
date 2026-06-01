import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import ( 
     mean_absolute_error,mean_squared_error,r2_score
)
df = pd.read_csv("Dataset.csv")
print("Loading Dataset...")
df = df.dropna(subset=["Aggregate rating"])
features = [
    "Votes",
    "Price range",
    "Has Table booking",
    "Has Online delivery"
]
le = LabelEncoder()
df["Has Table booking"] = le.fit_transform(df["Has Table booking"])
df["Has Online delivery"] = le.fit_transform(df["Has Online delivery"])
print("Preparing Features...")
X = df[features]
y = df["Aggregate rating"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
models = {
       "Linear Regression":LinearRegression(),"Decision Tree":DecisionTreeRegressor(random_state=42),"Random Forest":RandomForestRegressor(n_estimators=50,random_state=42)
}
print("\nModel Comparison")
results = {}
print("Training models...")
for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test,y_pred)
    rmse = np.sqrt(mean_squared_error(y_test,y_pred))
    r2 = r2_score(y_test,y_pred)
    results[name] = r2
    print(f"\n{name}")
    print(f"MAE       : {mae:.4f}")
    print(f"RMSE      : {rmse:.4f}")
    print(f"R2 Score  : {r2:.4f}")
best_model =  max(results,key=results.get)
print("\nBest Model:",best_model)
print("Best R2 Score:",round(results[best_model],4))




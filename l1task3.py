import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")
plt.figure(figsize=(10,6))
plt.scatter(
    df["Longitude"],
    df["Latitude"],
    alpha=0.5,
    s=25
)
city_counts = df["City"].value_counts().head(10)
print(city_counts)
plt.title("Geographic Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
correlation = df[
    ["Latitude",
     "Longitude",
     "Aggregate rating"]
].corr()
print("\nCorrelation Matrix")
print(correlation)

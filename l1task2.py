import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")
print("\nNumerical Statistics")
print(df.describe())
top_cities = df["City"].value_counts().head(10)
print("\nTop 10 Cities")
print(top_cities)
top_cuisines = df["Cuisines"].value_counts().head(10)
print("\nTop 10 Cuisines")
print(top_cuisines)
top_cities.plot(
    kind="bar",
    figsize=(10,5),
    title="Top Cities by Number of Restaurants"
)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")
most_common = df["Price range"].mode()[0]
print(f"\nMost Common Price Range : {most_common}")
avg_rating = (
    df.groupby("Price range")["Aggregate rating"].mean()
)
print("\nAverage Rating by Price Range")
print(avg_rating.round(2))
highest_color = avg_rating.idxmax()
print("\nColor with Highest Average Rating:",highest_color)
avg_rating.plot(
    kind="bar",
    figsize=(8,5)
)
plt.title("Average Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.show()
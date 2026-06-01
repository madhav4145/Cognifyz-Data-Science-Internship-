import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")
cuisine_rating = (
    df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)
)
print("\nTop Rated Cuisines")
print(cuisine_rating.head(10))
cuisine_votes = (
    df.groupby("Cuisines")["Votes"].sum().sort_values(ascending=False)
)
print("\nMost Popular Cuisines")
print(cuisine_votes.head(10))
top_rating = cuisine_rating.head(10)
most_votes = cuisine_votes.head(10)
top_rating.plot(kind="barh",figsize=(10,5))
plt.title("Top Rated Cuisines")
plt.show()
most_votes.plot(kind="barh",figsize=(10,5))
plt.title("Most Popular Cuisines")
plt.show()

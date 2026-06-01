import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")
plt.figure(figsize=(8,5))
sns.histplot(
    df["Aggregate rating"],
    bins=20,
    kde=True
)
plt.title("Distribution of Ratings")
plt.show()
plt.figure(figsize=(8,5))
sns.scatterplot( 
    x="Votes",
    y="Aggregate rating",
    data=df
)
plt.title("Votes vs Aggregate Rating")
plt.show()
plt.figure(figsize=(10,6))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()


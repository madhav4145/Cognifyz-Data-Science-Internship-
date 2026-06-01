import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("D:\Cognifyz Internship\Dataset.csv",encoding="latin-1")
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nDataset Information:")
print(df.info())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
numeric_columns = df.select_dtypes(include=["number"]).columns
text_columns = df.select_dtypes(include=["object","string"]).columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())
for column in text_columns:
    if not df[column].mode().empty:
       df[column] = df[column].fillna(df[column].mode()[0])
plt.figure(figsize=(8,5))
df["Aggregate rating"].hist(
    bins=20,
    edgecolor="black"
)
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.show()
print("\nAggregate Rating Counts:")
print(df["Aggregate rating"].value_counts())


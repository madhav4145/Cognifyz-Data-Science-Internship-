import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")
booking_percentage = (
    df["Has Table booking"].value_counts(normalize=True)* 100
)
print("\nTable Booking Percentage")
print(booking_percentage.round(2))
delivery_percentage = (
    df["Has Online delivery"].value_counts(normalize=True)* 100
)
print("\nOnline Delivery Percentage")
print(delivery_percentage.round(2))
rating_comparison = (
    df.groupby("Has Table booking")["Aggregate rating"].mean()
)
print("\nAverage Rating Comparison")
print(rating_comparison.round(2))
price_delivery = pd.crosstab(df["Price range"],df["Has Online delivery"])
print("\nOnline Delivery by Price Range")
print(price_delivery)
price_delivery.plot(kind="bar",figsize=(8,5))
plt.title("Online Delivery Availability by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.show()

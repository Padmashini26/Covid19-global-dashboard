# covid_dashboard.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("covid_data_sample.csv", parse_dates=["date"])

# Set style
sns.set(style="whitegrid")

# Plot 1: Total cases by country (latest date)
latest = df.groupby("location").last().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x="location", y="total_cases", data=latest)
plt.title("Total COVID-19 Cases by Country")
plt.ylabel("Total Cases")
plt.xlabel("Country")
plt.tight_layout()
plt.savefig("total_cases_by_country.png")
plt.show()

# Plot 2: New daily cases over time
plt.figure(figsize=(12, 6))
sns.lineplot(x="date", y="new_cases", hue="location", data=df)
plt.title("New COVID-19 Cases Over Time")
plt.ylabel("New Cases")
plt.xlabel("Date")
plt.tight_layout()
plt.savefig("new_cases_trend.png")
plt.show()

# Plot 3: Vaccination progress
plt.figure(figsize=(10, 5))
sns.barplot(x="location", y="total_vaccinations", data=latest)
plt.title("Total Vaccinations by Country")
plt.ylabel("Vaccinations")
plt.xlabel("Country")
plt.tight_layout()
plt.savefig("vaccination_progress.png")
plt.show()

print("Charts saved: total_cases_by_country.png, new_cases_trend.png, vaccination_progress.png")

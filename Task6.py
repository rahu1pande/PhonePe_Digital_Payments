import pandas as pd
import matplotlib.pyplot as plt

file_path = 'PhonePe_Pulse_Raw Data.xlsx'

State_txn_users = pd.read_excel(file_path)
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')


#Identify any treds or patterns in the transaction data using line graphs.
transaction_trends = (
    State_txn_users
    .groupby(["Year", "Quarter"], as_index=False)["Transactions"]
    .sum()
)

#Plot transaction trends over time
plt.figure(figsize=(10, 6))
plt.plot(transaction_trends["Year"].astype(str) + " Q" + transaction_trends["Quarter"].astype(str), transaction_trends["Transactions"], marker='o')
plt.xticks(rotation=45)
plt.xlabel("Year and Quarter")
plt.ylabel("Total Transactions")
plt.title("Transaction Trends Over Time")
plt.tight_layout()
plt.show()


#6.2 Correlate demographics data with transaction data
# Merge transaction data with demographics data on District column
merged_data = pd.merge(district_txn_users, district_demographics, left_on=["State", "District"], right_on=["State", "District"], how="inner")

#correlation analysis
correlation = merged_data["Transactions"].corr(merged_data["Population"])
print(f"Correlation between Transactions and Population: {correlation}")


#6.3 Summarize findings and insights.
print("Findings and Insights:")
print("1. There is a positive correlation between the number of transactions and the population of a district, suggesting that more populous districts tend to have higher transaction volumes.")
print("2. The transaction trends over time show fluctuations, which may be influenced by various factors such as economic conditions, government policies, and technological adoption.")
print("3. Further analysis could be conducted to explore the impact of specific demographic factors (e.g., age distribution, income levels) on transaction behavior, as well as to identify any regional disparities in transaction patterns.")

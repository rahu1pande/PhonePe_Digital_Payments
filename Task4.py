import pandas as pd
import matplotlib.pyplot as plt

file_path = 'PhonePe_Pulse_Raw Data.xlsx'
State_txn_users = pd.read_excel(file_path)
state_txnSplit = pd.read_excel(file_path, sheet_name='State_TxnSplit')
state_DeviceData = pd.read_excel(file_path, sheet_name='State_DeviceData')
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')

#4.1
#Aggregate total registered users at state level
state_users = (
    State_txn_users
    .groupby("State", as_index=False)["Registered Users"]
    .sum()
)

#Aggregate total population at state level
state_population = (
    district_demographics
    .groupby("State", as_index=False)["Population"]
    .sum()
)

#Merge both datasets
merged_df = state_users.merge(
    state_population,
    on="State",
    how="inner"
)

#Calculate ratio
merged_df["User_to_Population_Ratio"] = (
    merged_df["Registered Users"] / merged_df["Population"]
)

# Display tabular result
print(merged_df)

#Plot column chart
plt.figure()
plt.bar(merged_df["State"], merged_df["User_to_Population_Ratio"])
plt.xticks(rotation=45)
plt.xlabel("State")
plt.ylabel("User to Population Ratio")
plt.title("User to Population Ratio by State")
plt.tight_layout()
plt.show()


#4.2: Correlate population density with transaction volume
#MERGE district-level transaction data with district-level population data
merged_df = district_txn_users.merge(
    district_demographics,
    on=["State", "District"],
    how="inner"
)

#Aggregate transaction volume per district (if multiple rows exist)
district_totals = (
    merged_df
    .groupby(["State", "District"], as_index=False)
    .agg({
        "Transactions": "sum",
        "Density": "first"   # assuming density is constant per district
    })
)

#correlation
correlation = district_totals["Density"].corr(
    district_totals["Transactions"]
)

print("Correlation between Population Density and Transaction Volume:", correlation)

plt.figure()
plt.scatter(
    district_totals["Density"],
    district_totals["Transactions"]
)

plt.xlabel("Population_Density")
plt.ylabel("Transaction Volume")
plt.title("Population Density vs Transaction Volume")
plt.tight_layout()
plt.show()


#4.3 Average transaction amount per user
#Aggregate totals at state level
state_totals = (
    State_txn_users
    .groupby("State", as_index=False)
    .agg({
        "Amount (INR)": "sum",
        "Registered Users": "sum"
    })
)

#Calculate Average Transaction Amount per User
state_totals["Avg_Txn_Amount_Per_User"] = (
    state_totals["Amount (INR)"] /
    state_totals["Registered Users"]
)

# Display full table
print(state_totals)

#Top 5 Highest & # Lowest
top_5_highest = (
    state_totals
    .sort_values("Avg_Txn_Amount_Per_User", ascending=False)
    .head(5)
)

top_5_lowest = (
    state_totals
    .sort_values("Avg_Txn_Amount_Per_User", ascending=True)
    .head(5)
)

print("\nTop 5 States (Highest Avg Transaction per User):")
print(top_5_highest)

print("\nTop 5 States (Lowest Avg Transaction per User):")
print(top_5_lowest)


#4.4 Device brand usage ratio
#Aggregate total registered users per state
state_users = (
    State_txn_users
    .groupby("State", as_index=False)["Registered Users"]
    .sum()
)

#Aggregate device users per state and brand
device_usage = (
    state_DeviceData
    .groupby(["State", "Brand"], as_index=False)["Registered Users"]
    .sum()
)

#Merge datasets
merged_df = device_usage.merge(
    state_users,
    on="State",
    how="inner",
    suffixes=("_device", "_state")
)

#Calculate usage ratio
merged_df["Device_Usage_Ratio"] = (
    merged_df["Registered Users_device"] / merged_df["Registered Users_state"]
)

#Display tabular result
print(merged_df)

#Prepare data for bar chart
pivot_df = merged_df.pivot(
    index="State",
    columns="Brand",
    values="Device_Usage_Ratio"
)

#Plot bar chart
pivot_df.plot(kind="bar")

plt.xlabel("State")
plt.ylabel("Device Usage Ratio")
plt.title("Device Brand Usage Ratio by State")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
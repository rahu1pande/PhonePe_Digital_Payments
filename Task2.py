import pandas as pd
import matplotlib.pyplot as plt

file_path = 'PhonePe_Pulse_Raw Data.xlsx'
State_txn_users = pd.read_excel(file_path)
state_txnSplit = pd.read_excel(file_path, sheet_name='State_TxnSplit')
state_DeviceData = pd.read_excel(file_path, sheet_name='State_DeviceData')
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')

#2.1 Analyze transaction trends over the years for each state.
print("Total number of transactions and total transaction amount for each state over the years:")
print(State_txn_users.groupby(["State", "Year"]).agg({"Transactions": "sum", "Amount (INR)": "sum"}).reset_index())

print("Top 5 states with the highest transaction volumes:")
print(State_txn_users.groupby("State")["Transactions"].sum().reset_index().sort_values(by="Transactions", ascending=False).head(5)["State"].tolist(), end = "\n\n")

print("Top 5 states with the lowest transaction volumes:")
print(State_txn_users.groupby("State")["Transactions"].sum().reset_index().sort_values(by="Transactions").head(5)["State"].tolist())


#2.2 Identify the most common transaction types in each state and quarter.
print(state_txnSplit
      .groupby(["State", "Quarter", "Transaction Type"])["Transactions"]
      .sum()
      .reset_index()
      .sort_values(by="Transactions", ascending=False)
      .drop_duplicates(["State", "Quarter"])
      )


#2.3 Determine the device brand with the highest number of registered users in each satate.
print(state_DeviceData
      .groupby(["State", "Brand"])["Registered Users"]
      .sum()
      .reset_index()
      .sort_values(by="Registered Users", ascending=False)
      .drop_duplicates(["State"])
      )

#2.4 Create a list of the top disctrict per state based on population.
#For each sate identify the district with the highest population.
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')
top_districts = district_demographics.groupby(["State", "District"])["Population"].sum().reset_index().sort_values(by="Population", ascending=False).drop_duplicates(["State"])
print(top_districts)

#Column chart depicting the district with the highest population for each state.
plt.figure(figsize=(12, 6))
plt.bar(top_districts["State"], top_districts["Population"], color='skyblue')
plt.xlabel("State")
plt.xticks(rotation=90)
plt.tight_layout()
plt.ylabel("Population")
plt.title("District with the Highest Population for Each State")
plt.show()


#2.5 ATV for each state.
# compute the average transaction value for each state.
State_txn_users["ATV"] = State_txn_users["Amount (INR)"] / State_txn_users["Transactions"]
print(State_txn_users.groupby("State")["ATV"].mean().reset_index().sort_values(by="ATV"))

average_txn_value = (
    State_txn_users
    .groupby("State")
    .agg({
        "Amount (INR)" : "sum",
        "Transactions" : "sum"
    })
)

average_txn_value["ATV (INR)"] = average_txn_value["Amount (INR)"] / average_txn_value["Transactions"]
average_txn_value = average_txn_value.reset_index().reset_index()
print(average_txn_value[["State", "ATV (INR)"]])

#IDENTIFY top 5 states with the highest ATV and top 5 states with the lowest ATV.
print("Top 5 states with the highest ATV:")
print(average_txn_value.sort_values(by="ATV (INR)", ascending=False).head(5)[["State", "ATV (INR)"]], end = "\n\n")

print("Top 5 states with the lowest ATV:")
print(average_txn_value.sort_values(by="ATV (INR)").head(5)[["State", "ATV (INR)"]])


#2.6 Analyze app usage trends
#Total number of app open over the years and Quarter for each state.
print(State_txn_users.groupby(["State", "Year", "Quarter"])["App Opens"].sum().reset_index())

#identify trends in app usage by creating a line plot showing the number of app open over time for a selected state.
state_data = (
    State_txn_users
    .loc[State_txn_users["State"] == "Maharashtra"]
    .sort_values(by=["Year", "Quarter"])
    .assign(Time = lambda x: x["Year"].astype(str) + " Q" + x["Quarter"].astype(str))
)
plt.figure()
plt.plot(state_data["Time"], state_data["App Opens"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#2.7 Distribution of transaction types.
# Bar chart showing distribution of transaction types for each state
# for the most recent year and quarter in the dataset.
# Defensive selection of the most recent year and quarter
latest_year = state_txnSplit["Year"].max()
latest_quarter = state_txnSplit.loc[state_txnSplit["Year"] == latest_year, "Quarter"].max()

recent = state_txnSplit.loc[
    (state_txnSplit["Year"] == latest_year) & (state_txnSplit["Quarter"] == latest_quarter)
]

# Ensure Transactions is numeric and fill missing with 0
recent = recent.copy()
recent["Transactions"] = pd.to_numeric(recent["Transactions"], errors="coerce").fillna(0)

plot_df = (
    recent
    .groupby(["State", "Transaction Type"])["Transactions"]
    .sum()
    .unstack(fill_value=0)
)

ax = plot_df.plot(kind="bar", figsize=(12, 6))
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.tight_layout()
plt.show()


#2.8 find unique mapping between district names and district codes.
#Select district name and district code columns
district_mapping = district_txn_users[["District", "Code"]]

#Drop duplicate mappings
unique_mapping = district_mapping.drop_duplicates()

#Export to new CSV file
output_path = "D:/PhonePe_Digital_Payments/unique_district_mapping.csv"
unique_mapping.to_csv(output_path, index=False)

print("Done", output_path)


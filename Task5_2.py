import pandas as pd
import matplotlib.pyplot as plt

file_path = 'PhonePe_Pulse_Raw Data.xlsx'
State_txn_users = pd.read_excel(file_path)
state_txnSplit = pd.read_excel(file_path, sheet_name='State_TxnSplit')
state_DeviceData = pd.read_excel(file_path, sheet_name='State_DeviceData')
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')

#CREATE a pie chart showing the distribution of transaction types for a specific quarter & selected state.

selected_state = "Andaman & Nicobar Islands"
selected_year = 2020
selected_quarter = 1

#Filter data for the selected state, year, and quarter
filtered_data = state_txnSplit[
    (state_txnSplit["State"] == selected_state) &
    (state_txnSplit["Year"] == selected_year) &
    (state_txnSplit["Quarter"] == selected_quarter)
]

#Aggregate trransaction distribution
txn_distribution = (
    filtered_data
    .groupby("Transaction Type")["Transactions"]
    .sum()
    .reset_index()
)

#Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(txn_distribution["Transactions"], labels=txn_distribution["Transaction Type"], autopct='%1.1f%%')
plt.title(f"Transaction Type Distribution for {selected_state} in Q{selected_quarter} {selected_year}")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'PhonePe_Pulse_Raw Data.xlsx'
State_txn_users = pd.read_excel(file_path)
state_txnSplit = pd.read_excel(file_path, sheet_name='State_TxnSplit')
state_DeviceData = pd.read_excel(file_path, sheet_name='State_DeviceData')
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')

#Aggregate district-level data to state level
district_agg = (
    district_txn_users
    .groupby(["State", "Year", "Quarter"])
    .agg({
        "Transactions": "sum",
        "Amount (INR)": "sum",
        "Registered Users": "sum"
    })
    .reset_index()
)


# Aggregate state-level data
state_agg = (
    State_txn_users
    .groupby(["State", "Year", "Quarter"])
    .agg({
        "Transactions": "sum",
        "Amount (INR)": "sum",
        "Registered Users": "sum"
    })
    .reset_index()
)

#Merge both datasets
comparison = district_agg.merge(
    state_agg,
    on=["State", "Year", "Quarter"],
    suffixes=("_District", "_State")
)

#Identify discrepancies
discrepancies = comparison[
    (comparison["Transactions_District"] != comparison["Transactions_State"]) |
    (comparison["Amount (INR)_District"] != comparison["Amount (INR)_State"]) |
    (comparison["Registered Users_District"] != comparison["Registered Users_State"])
]

# Display discrepancies
print(discrepancies)

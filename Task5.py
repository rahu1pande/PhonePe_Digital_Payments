import pandas as pd
import matplotlib.pyplot as plt

file_path = 'PhonePe_Pulse_Raw Data.xlsx'
State_txn_users = pd.read_excel(file_path)
state_txnSplit = pd.read_excel(file_path, sheet_name='State_TxnSplit')
state_DeviceData = pd.read_excel(file_path, sheet_name='State_DeviceData')
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')

#DATA VISUALIZATION
#5.1 Plot the total transaction and amount over time for a selected state.
selected_state = "Andaman & Nicobar Islands"

state_data = (
    State_txn_users[State_txn_users["State"] == selected_state]
    .sort_values(by=["Year", "Quarter"])
    )

#create time label
state_data["Time"] = (
    state_data["Year"].astype(str) + " Q" + state_data["Quarter"].astype(str)
    )

#create plot with dual axis
fig, ax1 = plt.subplots(figsize=(10, 6))

#plot transaction
ax1.plot(state_data["Time"], state_data["Transactions"])
ax1.set_xlabel("Year and Quarter")
ax1.set_ylabel("Total Transactions")

#axis for amount
ax2 = ax1.twinx()
ax2.plot(state_data["Time"], state_data["Amount (INR)"])
ax2.set_ylabel("Total Amount (INR)")

plt.xticks(rotation=45)
plt.title(f"Total Transactions and Amount Over Time for {selected_state}")
plt.tight_layout()
plt.show()
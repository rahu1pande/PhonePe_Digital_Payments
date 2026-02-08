import pandas as pd

# Read the Excel file and load the data into a DataFrame
file_path = 'PhonePe_Pulse_Raw Data.xlsx'
state_txn_users = pd.read_excel(file_path)
# print(state_txn_users.head(10))
# print(state_txn_users.describe())
# print(state_txn_users.dtypes)
# print(state_txn_users.isnull().sum())
# print(state_txn_users.isnull().mean() * 100)
#print total number of states and total number of districts in the dataset.

#Load the state_txnSplit dataframe. 
state_txnSplit = pd.read_excel(file_path, sheet_name='State_TxnSplit')
# print(state_txnSplit.tail(10))
# print(state_txnSplit.describe())
# print(state_txnSplit.dtypes)
# print(state_txnSplit.isnull().sum())
# print(state_txnSplit.isnull().mean() * 100)



#Load the state_DeviceData dataframe.
state_DeviceData = pd.read_excel(file_path, sheet_name='State_DeviceData')
# middle_index = len(state_DeviceData) // 2
# print(state_DeviceData.iloc[int(middle_index - 5) : int(middle_index + 4 + 1)])
# print(state_DeviceData.describe())
# print(state_DeviceData.dtypes)
# print(state_DeviceData.isnull().sum())
# print(state_DeviceData.isnull().mean()* 100)



#Load the district_txn_users dataframe.
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')
# print(pd.concat([district_txn_users.head(10), district_txn_users.tail(10)]))
# print(district_txn_users.describe())
# print(district_txn_users.dtypes)
# print(district_txn_users.isnull().sum())
# print(district_txn_users.isnull().mean() * 100)


#load the District Demographics dataframe.
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')
# print(district_demographics[::10])
# print(district_demographics.describe())
# print(district_demographics.dtypes)
# print(district_demographics.isnull().sum())
# print(district_demographics.isnull().mean() * 100)

#print the total number of states and total number of districts in the dataset.
# print("Total number of states in the dataset:", district_demographics['State'].nunique())
# print("Total number of districts in the dataset:", district_demographics['District'].nunique())

#identify the state with highest number of districts.
state_with_most_districts = district_demographics['State'].value_counts().idxmax()
print("State with the highest number of districts:", state_with_most_districts)
import pandas as pd

# Read the Excel file and load the data into a DataFrame
file_path = 'PhonePe_Pulse_Raw Data.xlsx'
state_txn_users = pd.read_excel(file_path)

# Display first 10 rows of the state_txn_users dataframe
print(state_txn_users.head(10))
# Display statistical summary (mean, std, min, max, etc.)
print(state_txn_users.describe())
# Display data types of all columns
print(state_txn_users.dtypes)
# Display count of null/missing values for each column
print(state_txn_users.isnull().sum())
# Display percentage of null/missing values for each column
print(state_txn_users.isnull().mean() * 100)
# Display the count of unique states in the dataset
print("Total number of states in the dataset:", state_txn_users['State'].nunique())

#Load the state_txnSplit dataframe. 
state_txnSplit = pd.read_excel(file_path, sheet_name='State_TxnSplit')
# Display last 10 rows of the state_txnSplit dataframe
print(state_txnSplit.tail(10))
# Display statistical summary (mean, std, min, max, etc.)
print(state_txnSplit.describe())
# Display data types of all columns
print(state_txnSplit.dtypes)
# Display count of null/missing values for each column
print(state_txnSplit.isnull().sum())
# Display percentage of null/missing values for each column
print(state_txnSplit.isnull().mean() * 100)


#Load the state_DeviceData dataframe.
state_DeviceData = pd.read_excel(file_path, sheet_name='State_DeviceData')
middle_index = len(state_DeviceData) // 2
# Display rows around the middle of the state_DeviceData dataframe
print(state_DeviceData.iloc[int(middle_index - 5) : int(middle_index + 4 + 1)])

# Display statistical summary (mean, std, min, max, etc.)
print(state_DeviceData.describe())

# Display data types of all columns
print(state_DeviceData.dtypes)

# Display count of null/missing values for each column
print(state_DeviceData.isnull().sum())

# Display percentage of null/missing values for each column
print(state_DeviceData.isnull().mean()* 100)


#Load the district_txn_users dataframe.
district_txn_users = pd.read_excel(file_path, sheet_name='District_Txn and Users')

# Display first 10 and last 10 rows
print(pd.concat([district_txn_users.head(10), district_txn_users.tail(10)]))

# Display statistical summary (mean, std, min, max, etc.)
print(district_txn_users.describe())

# Display data types of all columns
print(district_txn_users.dtypes)

# Display count of null/missing values for each column
print(district_txn_users.isnull().sum())

# Display percentage of null/missing values for each column
print(district_txn_users.isnull().mean() * 100)


#load the District Demographics dataframe.
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')

# Display every 10th row of the district_demographics dataframe
print(district_demographics[::10])

# Display statistical summary (mean, std, min, max, etc.)
print(district_demographics.describe())

# Display data types of all columns
print(district_demographics.dtypes)

# Display count of null/missing values for each column
print(district_demographics.isnull().sum())

# Display percentage of null/missing values for each column
print(district_demographics.isnull().mean() * 100)

#print the total number of states and total number of districts in the dataset.
print("Total number of states in the dataset:", district_demographics['State'].nunique())
print("Total number of districts in the dataset:", district_demographics['District'].nunique())

#identify the state with highest number of districts.
state_with_most_districts = district_demographics['State'].value_counts().idxmax()
print("State with the highest number of districts:", state_with_most_districts)
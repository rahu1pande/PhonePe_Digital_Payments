#A bar plot showing the population density of districts in a selected state.
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'PhonePe_Pulse_Raw Data.xlsx'
district_demographics = pd.read_excel(file_path, sheet_name='District Demographics')

selected_state = "Bihar"
state_districts = district_demographics[district_demographics["State"] == selected_state]

plt.figure()
plt.bar(state_districts["District"], state_districts["Density"])
plt.xticks(rotation=45)
plt.xlabel("District")
plt.ylabel("Population Density")
plt.title(f"Population Density of Districts in {selected_state}")
plt.tight_layout()
plt.show()
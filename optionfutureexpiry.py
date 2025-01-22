# Step 1: Download the Current_Option_Expiry list
import pandas as pd

# URL of the API endpoint
url = "https://api.kite.trade/instruments"

# Fetch and preprocess the data
data = pd.read_csv(url)
data['expiry'] = pd.to_datetime(data['expiry']).dt.strftime('%d-%m-%Y')

# Define filter conditions
filters = [
    {"filter_names_list": ["NIFTY", "BANKNIFTY", "FINNIFTY"], "segment": "NFO-OPT"},
    {"filter_names_list": ["SENSEX", "BANKEX"], "segment": "BFO-OPT"}  
]

# Initialize an empty DataFrame to store the results
combined_filtered_data = pd.DataFrame()

# Apply the filters and process data
for f in filters:
    for name in f["filter_names_list"]:
        # Apply filter condition for each name in the list
        filtered_data = data[data['name'].str.contains(name) & (data['segment'] == f["segment"])]
        filtered_data = filtered_data.loc[:, ["name", "expiry", "lot_size"]]
        filtered_data['current_expiry'] = filtered_data['name'] + "|" + filtered_data['expiry']
        combined_filtered_data = pd.concat([combined_filtered_data, filtered_data.head(1)])

# Save to Excel
combined_filtered_data.to_excel("expiry.xlsx", index=False)







# Define filter conditions
filters = [
    {"filter_names_list": ["NIFTY", "BANKNIFTY", "FINNIFTY"], "segment": "NFO-FUT"},
    {"filter_names_list": ["CRUDEOIL", "GOLD", "SILVER"], "segment": "MCX-FUT"},
    {"filter_names_list": ["SENSEX", "BANKEX"], "segment": "BFO-FUT"},
]

# Initialize an empty DataFrame to store the results
combined_filtered_data = pd.DataFrame()

# Apply the filters and process data
for f in filters:
    for name in f["filter_names_list"]:
        # Apply filter condition for each name in the list
        filtered_data = data[data['name'].str.contains(name) & (data['segment'] == f["segment"])]
        filtered_data = filtered_data.loc[:, ["name", "expiry", "lot_size"]]
        filtered_data['current_expiry'] = filtered_data['name'] + "|" + filtered_data['expiry']
        combined_filtered_data = pd.concat([combined_filtered_data, filtered_data.head(1)])

# Filter further based on selected names
filter_names = ["NIFTY", "BANKNIFTY", "FINNIFTY", "CRUDEOIL", "SENSEX", "BANKEX"]
final_filtered_df = combined_filtered_data[combined_filtered_data['name'].isin(filter_names)]

# Display the final filtered dataframe
print(final_filtered_df)

# Save the filtered data to a single Excel file
final_filtered_df.to_excel('future_expiry.xlsx', index=False)

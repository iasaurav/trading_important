# Step 1: Download the Nifty 500 list
import requests
url = "https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv"
headers = {'User-Agent': 'Mozilla/5.0'}

# Download and save CSV
response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open("nifty500.csv", "wb") as file:
        file.write(response.content)
else:
    print("Download failed.")


# Step 2: Download the Option_Expiry list
import pandas as pd

# URL of the API endpoint
url = "https://api.kite.trade/instruments"

# Fetch and preprocess the data
data = pd.read_csv(url)
data['expiry'] = pd.to_datetime(data['expiry']).dt.strftime('%d-%m-%Y')

# Define filter conditions
filters = [
    {"filter_names_list": ["NIFTY", "BANKNIFTY", "FINNIFTY"], "segment": "NFO-OPT"},
    {"filter_names_list": ["SENSEX", "BANKEX"], "segment": "BFO-OPT"},
    {"filter_names_list": ["CRUDEOIL", "GOLD", "SILVER"], "segment": "MCX-OPT"},

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
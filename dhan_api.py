import pandas as pd

# Read the CSV file from the URL
data = pd.read_csv("https://images.dhan.co/api-data/api-scrip-master-detailed.csv")

# Select the first 15 columns
data = data.iloc[:, :15]

# Define access token and client ID
client_id = "api"      # Your client ID
access_token = "bihar"  # Your access token

# Add new columns
data['client_id'] = client_id
data['access_token'] = access_token

# Format and rename the SM_EXPIRY_DATE column
data['SM_EXPIRY_DATE'] = pd.to_datetime(data['SM_EXPIRY_DATE'], errors='coerce').dt.strftime('%d-%m-%Y')
data.rename(columns={'SM_EXPIRY_DATE': 'EXPIRY_DATE'}, inplace=True)

# Save the processed DataFrame to an Excel file
data.to_excel('dhan_options.xlsx', index=False)

# Print the processed DataFrame
print(data)

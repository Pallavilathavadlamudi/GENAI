import pandas as pd # Data Manipulation and Analysis
import numpy as np  # Numerical Expressions
import re # Regular Expressions
from sqlalchemy import create_engine #interacting with databases & create engine connects to database 

#1. Load csv file into database in dataintodatabase.py

#2. Connect to PostgreSQL database
engine = create_engine('postgresql://admin:Admin%40043@localhost:5432/ecommerce')

#3. Read data from PostgreSQL
Amazondata = pd.read_sql("SELECT * FROM amazon_sale_report",engine)

# 4. Understanding the data

    # 1. Shape of the dataset
print("\nData Overview:\n")
print("Shape of the dataset:", Amazondata.shape, "\n")

    # 2. Schema of the data
Amazondataschema = pd.DataFrame({
    'Column Name': Amazondata.columns,
    'Data Type': Amazondata.dtypes.values,
    'Missing Values': Amazondata.isnull().sum().values,
    'Unique Values': Amazondata.nunique().values,
}) 

print("\nDataset Schema:")
print(Amazondataschema)

print("\nOutput: ")
print(Amazondata.describe())

    # Print head and tail of the dataframe
print("\nData head:\n", Amazondata.head(), "\n")
print("Data tail:\n", Amazondata.tail(), "\n")

    # Value Counts for Categorical Columns
'   ''This loops through all object (string) columns in the DataFrame and prints the top 10 most frequent values for each'''
for col in Amazondata.select_dtypes(include='object').columns:
    print(f"\nValue counts for '{col}':")
    print(Amazondata[col].value_counts().head(10))

    # 5. unique values for key columns
    # Understanding column data

    # 1. Strip column names (just for safety)
Amazondata.columns = Amazondata.columns.str.strip()

    # 2. Define a helper function to print unique values
def print_unique_values(column_name):
    if column_name in Amazondata.columns:
        print(f"\nColumn: '{column_name}'")
        print("Unique Count:", Amazondata[column_name].nunique())
        print("Unique Values:", Amazondata[column_name].dropna().unique()[:50])  # Limit to 50 for readability
    else:
        print(f"\nColumn '{column_name}' not found in the dataset.")

    # 3. List of columns to analyze
columns_to_check = [
    'Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel',
    'ship-service-level', 'Style', 'SKU', 'Category', 'Size',
    'ASIN', 'Courier Status', 'Qty', 'currency', 'Amount',
    'ship-city', 'ship-state', 'ship-postal-code', 'ship-country',
    'promotion-ids', 'B2B', 'fulfilled-by', 'Unnamed: 22'
]

    # 4. Print unique values for each column
for column in columns_to_check:
    # Clean string columns before checking
    if Amazondata[column].dtype == 'object':
        Amazondata[column] = Amazondata[column].astype(str).str.strip()
    print_unique_values(column)

# 5. DATA CLEANING 
    ''' 1) Remove Duplicates
        2) Fix Structural Errors
        3) Filter Unwanted Outliers
        4) Handle Missing Values
        5) Validate Q&A '''

    # 1. Remove Duplicates

    # 1. Identify duplicates based on Order ID, SKU, Qty, and Date
Amazon_duplicates = Amazondata[Amazondata.duplicated(subset=['Order ID', 'SKU', 'Qty', 'Date'], keep=False)]

print("\nTotal duplicate rows found:", Amazon_duplicates.shape[0])
print(Amazon_duplicates)

    # 2. Count rows before dropping duplicates
rows_before = Amazondata.shape[0]

    # 3. Drop duplicates (keep only the first occurrence)
Amazondata = Amazondata.drop_duplicates(subset=['Order ID', 'SKU', 'Qty', 'Date'], keep='first')

    # 4. Count rows after dropping
rows_after = Amazondata.shape[0]
rows_removed = rows_before - rows_after

    # 5. Show how many rows were removed
print(f"\nRemoved {rows_removed} duplicate rows.")

    # 6. Preview the cleaned dataset
print("\nCleaned Dataset Preview:")
print("Shape of the cleaned dataset:", Amazondata.shape)
print("\nFirst 5 rows:")
print(Amazondata.head())

    # 2. Remove Unwanted Columns

# drop unnames:_22 column ; fulfilled-by ; courier status
Amazondata.drop(columns=['Unnamed: 22'], inplace=True)
Amazondata.drop(columns=['fulfilled-by'], inplace=True)
Amazondata.drop(columns=['Courier Status'],inplace=True)

# checking after dropping the column
print("Columns after removing 'unnamed: 22 , fulfilled-by and Courier Status':\n")
print(Amazondata.columns.tolist())

    # 3. Merge Currency and Amount columns into single column

# 1. Clean column names (if not already done)
Amazondata.columns = Amazondata.columns.str.strip().str.lower().str.replace('-', '_')

# 2. Merge 'currency' and 'amount' into one formatted 'amount' column
Amazondata['amount'] = Amazondata.apply(
    lambda row: f"{row['currency']} {row['amount']}" if pd.notnull(row['amount']) and pd.notnull(row['currency']) else np.nan,
    axis=1
)

print("\nAfter Merging:", Amazondata.columns)

# 3. Handle nulls in 'amount'
# If status is 'Cancelled' → assign '0'
# If status is 'Shipped' (or similar), leave as NaN (you'll fill with mean/mode later)

Amazondata['amount'] = Amazondata.apply(
    lambda row: '0' if pd.isnull(row['amount']) and 'cancelled' in str(row['status']).lower() else row['amount'],
    axis=1
)

# 4. Drop the 'currency' column
Amazondata.drop(columns=['currency'], inplace=True)

# 5. Preview result
print("\nUpdated 'amount' column and removed 'currency':")
print(Amazondata[['status', 'amount']].head())

    # 2. Fix Structural Errors

    # 1. check for extra spaces in column names

# 1. Print original column names (to show before cleaning)
print("\nOriginal Column Names: \n")
for column in Amazondata.columns:
    print(f"'{column}'")

# 2. Clean column names:
# - Strip leading/trailing whitespace
# - Replace spaces with underscores
# - Convert to lowercase
Amazondata.columns = (
    Amazondata.columns
    .str.strip()              # Remove leading/trailing spaces
    .str.replace(' ', '_')    # Replace inner spaces with underscores
    .str.replace('-', '_')    # Replace hyphens with underscores
    .str.lower()              # Convert to lowercase
)

# 3. Print cleaned column names
print("\nCleaned Column Names:  ")
for column in Amazondata.columns:
    print(column)

# 4. Preview the cleaned dataset
print("\nPreview of Cleaned Data:")
print(Amazondata.head())

    # 2. Mixed Data Types

# 1. Changing the data type of data column from object to datetime
Amazondata['date'] = pd.to_datetime(Amazondata['date'],errors='coerce')

# check if the conversion was successful
print("\nData type of 'date' column after conversion:", Amazondata['date'].dtype)

# 2. Changing the data type of 'ship_postal_code' column from int64 to string
# This is useful if postal codes can have leading zeros or special characters
Amazondata['ship_postal_code'] = Amazondata['ship_postal_code'].astype('Int64').astype(str)

# check if the conversion was successful
print("\nData type of 'ship_postal_code' column after conversion:", Amazondata['ship_postal_code'].dtype)

#3. Identify and fix inconsistent data entries

# 1.check for inconsistent date formats
print("\nchecking for inconsistent date formats in the 'date' columns:")
Amazondata['date'] = pd.to_datetime(Amazondata['date'], format='%m-%d-%y', errors='coerce')
Amazondata['date'] = Amazondata['date'].dt.strftime('%m-%d-%Y')

# check for conversion issues
invalid_dates = Amazondata[Amazondata['date'].isna()]
print(f"Invalid Dates Found: {len(invalid_dates)}")

# 2. Maping the 'Status column' to a consistent format
''' Shipped - Delivered to Buyer-Delivered
   Shipped, Shipping, Shipped - Out for Delivery, Shipped - In Transit
   Shipped - Lost in Transit, Shipped - Damaged
   Shipped - Returned to Seller, Shipped - Rejected by Buyer, Shipped - Returning to Seller - Returned
   Cancelled - Cancelled
   Pending, Pending - Waiting for Pick Up- pending '''

status_map = {
    'Shipped - Delivered to Buyer': 'Delivered',
    'Shipped': 'In Transit',
    'Shipping': 'In Transit',
    'Shipped - Out for Delivery': 'In Transit',
    'Shipped - Picked Up': 'In Transit',
    'Shipped - Returned to Seller': 'Returned',
    'Shipped - Rejected by Buyer': 'Returned',
    'Shipped - Returning to Seller': 'Returned',
    'Shipped - Lost in Transit': 'Damaged',
    'Shipped - Damaged': 'Damaged',
    'Cancelled': 'Cancelled',
    'Pending': 'Pending',
    'Pending - Waiting for Pick Up': 'Pending'
}

Amazondata['status'] = Amazondata['status'].map(status_map)

#print unique vales in the status column after updating
print("\n Unique values in the 'status' column:")
print(Amazondata['status'].unique())
         
#3. check for the inconsistent fullfilment column

#View Raw Counts
print("Original value counts in 'Fulfilment':")
print(Amazondata['fulfilment'].value_counts(dropna=False))

#clean column 
Amazondata['fulfilment'] = Amazondata['fulfilment'].astype(str).str.strip().str.title()

#Reckeck the column after cleaning
print("\nCleaned unique values in 'Fulfilment':")
print(Amazondata['fulfilment'].unique())

#4. check for non Amazon rows in Sales channel
non_amazon_rows = Amazondata[Amazondata['sales_channel'] == 'Non-Amazon']
print(f"🔎 Total Non-Amazon rows: {len(non_amazon_rows)}")
print(non_amazon_rows.head())  # show first few rows

#4. Check for the inconsistent data from Ship_city

# STEP 1: Standardize capitalization and strip extra spaces
Amazondata['ship_city'] = Amazondata['ship_city'].astype(str).str.strip().str.title()

print("\nUpdated Unique Cities (After Initial Standardization):\n")
print(Amazondata['ship_city'].unique())

# STEP 2: Clean raw city strings
def clean_raw_city(city):
    if pd.isna(city):
        return city
    city = str(city).lower().strip()
    city = re.sub(r'[^\w\s]', '', city)       # remove punctuation
    city = re.sub(r'\s+', ' ', city)          # collapse multiple spaces
    return city.title()  # Reformat to title case

Amazondata['ship_city'] = Amazondata['ship_city'].apply(clean_raw_city)

# Print cleaned unique cities
print("\n Cleaned Unique Cities:")
print(Amazondata['ship_city'].unique())

# STEP 3: Drop cities with fewer than 50 occurrences
city_counts = Amazondata['ship_city'].value_counts()
valid_cities = city_counts[city_counts >= 50].index
Amazondata = Amazondata[Amazondata['ship_city'].isin(valid_cities)]

# STEP 4: Drop rows where city names contain digits (e.g., "Sector 10")
# '~' Removes the names like Sector 10, Area 5, Block 12
Amazondata = Amazondata[~Amazondata['ship_city'].str.contains(r'\d', na=False)]

# Final result
''' Counting and listing the unique values and its occurances '''
# Final counts (if needed)
city_counts = Amazondata['ship_city'].value_counts()
print("City Counts (≥50 occurrences):")
print(city_counts.head(10))

# Print total number of unique cities
print(f"Total Unique Cities: {city_counts.shape[0]}")

# Display all city names with their counts
print("City-wise Order Counts:")
for city, count in city_counts.items():
    print(f"{city}: {count}")

# Check for the inconsistent data from Ship_city

# STEP 1: Standardize capitalization and strip extra spaces
Amazondata['ship_state'] = Amazondata['ship_state'].astype(str).str.strip().str.title()

# STEP 2: Get state value counts
state_counts = Amazondata['ship_state'].value_counts()

# STEP 3: Keep only states with ≥ 5 occurrences
valid_states = state_counts[state_counts >= 5].index
Amazondata = Amazondata[Amazondata['ship_state'].isin(valid_states)]

# STEP 4: Recalculate counts after filtering
state_counts = Amazondata['ship_state'].value_counts()

# Final counts (if needed)
print("\nState Counts (≥5 occurrences):")
print(state_counts.head(10))

# Print total number of unique states
print(f"\nTotal Unique States (after filter): {state_counts.shape[0]}")

# Display all state names with their counts
print("\nState-wise Order Counts:")
for state, count in state_counts.items():
    print(f"{state}: {count}")

# checking for ship-postal-code
# STEP 1: Convert 'ship-postal-code' to string (remove decimal if needed)
Amazondata['ship_postal_code'] = Amazondata['ship_postal_code'].astype(str).str.split('.').str[0]

# STEP 2: Filter only rows where postal code has exactly 6 digits
Amazondata = Amazondata[Amazondata['ship_postal_code'].str.len() == 6]

# STEP 3: Optional — remove any rows with non-digit postal codes (just in case)
Amazondata = Amazondata[Amazondata['ship_postal_code'].str.isdigit()]

# Final check
print(f"\nRemaining rows: {len(Amazondata)}")
print(f"\nUnique Postal Codes: {Amazondata['ship_postal_code'].nunique()}")
print("\nSample Postal Codes:", Amazondata['ship_postal_code'].unique()[:10])

    # 3. How to Handle Missing Values

# List of the 4 shipping columns
shipping_columns = ['ship_city', 'ship_state', 'ship_postal_code', 'ship_country']

# Drop rows where all 4 are missing (NaN)
Amazondata = Amazondata.dropna(subset=shipping_columns, how='all')

print(f"✅ Remaining rows after dropping if all 4 ship fields are missing: {Amazondata.shape[0]}")

print(Amazondata.shape)

# Define the shipping-related columns
shipping_columns = ['ship_city', 'ship_state', 'ship_postal_code', 'ship_country']

# Drop rows where any of the columns are missing
Amazondata = Amazondata.dropna(subset=shipping_columns, how='any')

print(f"✅ Remaining rows after dropping rows with any missing shipping fields: {Amazondata.shape[0]}")
print(Amazondata.shape)

'''Cleans the amount values by removing currency symbols.
Fills in missing prices based on matching SKU.
Restores the currency format as 'INR xxx.xx'''

# Step 1: Extract numeric amount if it's a string (e.g., "INR 500")
Amazondata['amount'] = Amazondata['amount'].str.extract(r'(\d+\.?\d*)').astype(float)

# Step 2: Fill missing 'amount' using other rows with same SKU
Amazondata['amount'] = Amazondata.groupby('sku')['amount'].transform(lambda x: x.ffill().bfill())

# Step 3: Reformat to INR string
Amazondata['amount'] = 'INR ' + Amazondata['amount'].round(2).astype(str)

# Print sample to verify
print("\nFilled Amounts by SKU:")
print(Amazondata[['sku', 'amount']].head(10))

# Final Check Schema of the DataSet Updated
Amazondataschema = pd.DataFrame({
    'Column Name': Amazondata.columns,
    'Data Type': Amazondata.dtypes.values,
    'Missing Values': Amazondata.isnull().sum().values,
    'Unique Values': Amazondata.nunique().values,
}) 

print("\nDataset Schema:")
print(Amazondataschema)
print(Amazondata.columns)

print(Amazondata.shape)


# Write DataFrame to a new table (or replace existing one)
Amazondata.to_sql(
    name='cleaned_amazon_sale_report',  # New table name
    con=engine,
    if_exists='replace',               # Options: 'fail', 'replace', 'append'
    index=False                        # Don't include the pandas index as a column
)

print("\nCleaned DataFrame has been successfully uploaded to PostgreSQL as 'cleaned_amazon_sale_report'")


import pandas as pd 
from sqlalchemy import create_engine

#1. Load csv file into database in AmazonDataCleaning.py
#2. Connect to PostgreSQL database
engine = create_engine('postgresql://admin:Admin%40043@localhost:5432/ecommerce')

#3. Read data from PostgreSQL
Amazondata = pd.read_sql("SELECT * FROM cleaned_amazon_sale_report",engine)

# 4. Drop the 'index' column if it exists
if 'index' in Amazondata.columns:
    Amazondata = Amazondata.drop(columns=['index'])

# 5. Schema of the data
Amazondataschema = pd.DataFrame({
    'Column Name': Amazondata.columns,
    'Data Type': Amazondata.dtypes.values,
    'Missing Values': Amazondata.isnull().sum().values,
    'Unique Values': Amazondata.nunique().values,
}) 

print("\nDataset Schema:")
print(Amazondataschema)
print(Amazondata.shape)

# 6. Sorting operations

# 1. Sort the dataframe accoring to the dates in ascending order and resetting the index after sorting

# Ensure 'date' column is datetime type (safety check)
Amazondata['date'] = pd.to_datetime(Amazondata['date'], errors='coerce')

# Sort by date (ascending = earliest first)
Amazondata = Amazondata.sort_values(by='date', ascending=True)

# Reset index after sorting
Amazondata = Amazondata.reset_index(drop=True)

# Convert datetime to date only (after sorting and resetting index)
Amazondata['date'] = Amazondata['date'].dt.date


# 2. Reordering the columns
# Define your desired column order
desired_column_order = [
    'date', 'order_id', 'asin', 'style', 'sku', 'category', 'size',
    'qty', 'amount', 'ship_city', 'ship_state', 'ship_postal_code', 'ship_country',
    'status', 'ship_service_level', 'promotion_ids', 'fulfilment', 'b2b'
]

# Reorder the DataFrame columns accordingly
# This keeps only columns in the desired list, ignoring any extras
Amazondata = Amazondata[desired_column_order]

print("Columns after reordering:")
print(Amazondata.columns.tolist())

# Replacing Column Names
Amazondata.rename(columns={
    'qty': 'quantity',
    'sku': 'stock_keeping_unit',
    'asin': 'amazon_standard_identification_number',
    'status': 'courier_status',
    'category': 'product_category'
}, inplace=True)

print(Amazondata.columns.tolist())

# replace the existing table in the database
Amazondata.to_sql(
    name='cleaned_amazon_sale_report',
    con=engine,
    if_exists='replace',  # This DROPS the old table and recreates it with new data and structure
    index=False
)
print("Existing table 'cleaned_amazon_sale_report' replaced with updated data.")


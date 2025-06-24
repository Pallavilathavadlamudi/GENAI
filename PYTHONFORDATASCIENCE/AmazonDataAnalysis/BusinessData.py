import pandas as pd
import re
from sqlalchemy import create_engine

#1. Load csv file into database in AmazonDataSorting.py

#2. Connect to PostgreSQL database
engine = create_engine('postgresql://admin:Admin%40043@localhost:5432/ecommerce')

#3. Read data from PostgreSQL
Amazondata = pd.read_sql("SELECT * FROM cleaned_amazon_sale_report",engine)

#1. BR:1 Identify top-selling product categories and their performance by region. (Category_sales_by_state)

# Ensure 'amount' is numeric (remove 'INR ' if needed)
Amazondata['amount'] = Amazondata['amount'].str.extract(r'(\d+\.?\d*)').astype(float)

# Filter only successful deliveries
delivered_data = Amazondata[Amazondata['courier_status'] == 'Delivered']

# Group by product category and region (e.g., ship_state)
summary_table = delivered_data.groupby(
    ['product_category', 'ship_state']
).agg(
    total_quantity=('quantity', 'sum'),
    total_sales=('amount', 'sum'),
    order_count=('order_id', 'count')  # optional: number of orders
).reset_index()

# Sort by total sales (descending)
product_performance = summary_table.sort_values(by='total_sales', ascending=False)

# Save the grouped summary table to the database
product_performance.to_sql(
    name='category_sales_by_state',  # 🚨 Your new table name
    con=engine,
    if_exists='replace',            # 'replace' overwrites if the table exists
    index=False                     # Don't store pandas index as a column
)

print("Summary table saved to database as 'category_sales_by_state'")

# BR:2 Evaluate order delivery performance by fulfillment type and courier status(delivery_performance_data)

# STEP 1: Select only the required columns 
required_columns = ['date', 'order_id', 'fulfilment', 'courier_status']
filtered_data = Amazondata[required_columns]

# STEP 2: Sort by fulfilment and courier status
sorted_filtered_data = filtered_data.sort_values(by=['fulfilment', 'courier_status'])

# STEP 3: Save to new table in the database
sorted_filtered_data.to_sql(
    name='delivery_performance_data',  # Your new table name
    con=engine,
    if_exists='replace',              # Overwrites existing table
    index=False
)

print("\nFiltered and sorted delivery data saved to 'delivery_performance_data' in the database.")

#BR 3: Identify regional trends and customer types(egional_trends_customer_types)

# STEP 1: Select required columns for BR3
columns_br3 = [
    'date',
    'order_id',
    'ship_city',
    'ship_state',
    'ship_country',
    'b2b',
    'amount',
    'product_category'  # Only if already renamed from 'category'
]

# ✅ Make a deep copy to avoid SettingWithCopyWarning
br3_data = Amazondata[columns_br3].copy()

# STEP 2: Clean and convert 'amount' to float (safely)
br3_data['amount'] = br3_data['amount'].astype(str).str.extract(r'(\d+\.?\d*)')[0].astype(float)

# STEP 3: Sort the data by region and customer type
br3_data = br3_data.sort_values(by=['ship_state', 'b2b'])

# STEP 4: Save the cleaned table to the database
br3_data.to_sql(
    name='regional_trends_customer_types',
    con=engine,
    if_exists='replace',
    index=False
)

print("\nBR3 table saved as 'regional_trends_customer_types' in the database.")

# Summary of Data Analysis and Cleaning for Amazon Sale Report

1. Files Analyzed:

    * dataintodatabase.py – Loads cleaned data into PostgreSQL.
    * AmazonDataCleaning.py – Performs full data cleaning.
    * AmazonDataSorting.py – Handles sorting, aggregation, and insights.
    * BusinessData.py – Extracts business-related summaries.

# CODE FILE EXPLANATIONS

1. dataintodatabase.py

    1. Load CSV File
        Reads the file "Amazon Sale Report.csv" from the local system using pandas.

    2. Connect to PostgreSQL
        Establishes a connection to the ecommerce database using SQLAlchemy.
        Uses a URL-encoded password (Admin@0043 → Admin%40043).

    3. Upload Data to Database
        Writes the DataFrame to a table named amazon_sale_report in the database.
        If the table already exists, it is replaced.

2. AmazonDataCleaning.py

    File Purpose:

    This script is designed to clean, standardize, and transform raw Amazon sales data retrieved from a PostgreSQL database. The final cleaned dataset is saved back to the database as cleaned_amazon_sale_report.

    Step-by-Step Breakdown
    
    1. Data Loading & Exploration

        Connects to PostgreSQL and loads the raw amazon_sale_report table into a Pandas DataFrame.
        Displays dataset shape, schema (data types, null counts, unique values), and basic statistics.
        Prints sample values for all categorical columns.

    2. Data Cleaning Process

        1. Remove Duplicates
            Identifies and removes duplicate rows based on Order ID, SKU, Qty, and Date.

        2. Drop Unwanted Columns
        
            Drops the following:
            Unnamed: 22 (empty/unused column),
            fulfilled-by (assumed duplicate of fulfilment),
            Courier Status (replaced by status).
    
        3. Merge Currency and Amount
            Combines currency and amount into a single field:
            Format: "INR 500"
            Sets amount to 0 if status = "Cancelled".
            Drops the old currency column.
    
    3. Fix Structural Errors

        1. Column Name Normalization
            Standardizes column names: lowercase, underscores instead of spaces/hyphens.
        
        2. Data Type Corrections
            
            Converts:
            date → datetime,
            ship_postal_code → string (to preserve formatting like leading 0s).
       
        3. Standardize Status Values
            Maps variations of shipment statuses into unified categories like:
            Delivered, In Transit, Returned, Damaged, Cancelled, Pending.

        4. Clean 'Fulfilment' and 'Sales Channel'
            Strips and title-cases values.
            Identifies and reports non-Amazon sales entries.

        5. Clean 'Ship City' and 'Ship State'
            Standardizes formatting and removes:
            Cities with <50 records,
            Cities containing numbers (e.g., "Sector 10").
            Removes states with <5 records.

        6. Clean 'Ship Postal Code'
            Ensures all postal codes:
            Are 6-digit numeric strings.
            Excludes any malformed values.

    4. Handle Missing Values

        Drops rows where all 4 shipping fields (ship_city, ship_state, ship_postal_code, ship_country) are missing.
        Further removes rows where any of the shipping fields are missing.
    
    5. Impute and Format 'Amount' Values

        Extracts numeric part from the amount string.
        Fills missing amount values using forward/backward fill by SKU.
        Re-formats as "INR xxx.xx" string.

    6. Schema Revalidation and Save

        Recalculates and prints updated schema summary.
        Writes the cleaned dataset back to the database as cleaned_amazon_sale_report.

| **Data Quality Dimension** | **How It's Achieved**                                                   |
| -------------------------- | ----------------------------------------------------------------------- |
| Validity                   | Type conversions (e.g., date, postal code), valid ranges for amount     |
| Accuracy                   | Manual standardization (e.g., status mapping), deduplication            |
| Completeness               | Null handling and imputation strategies                                 |
| Consistency                | Uniform naming, normalized values across key columns                    |
| Uniformity                 | Currency format, city/state casing, column names formatted consistently |

3. AmazonDataSorting.py

    1. Load Cleaned Data:
        Connects to the PostgreSQL database using SQLAlchemy.
        Loads the cleaned_amazon_sale_report table into a Pandas DataFrame.
    
    2. Preprocessing:
        Drops the 'index' column if it exists (possibly leftover from previous saves).
        Creates and prints a schema summary: column names, data types, null count, and unique value count.

    3. Sorting by Date:
        Converts the date column to proper datetime format.
        Sorts the records in ascending order of dates.
        Resets the index to match the new order.
        Converts datetime back to date only (YYYY-MM-DD).
    
    4. Reorganizing Columns:
        Defines a preferred order of columns (e.g., date, order_id, sku, qty, etc.).
        Filters and reorders the DataFrame accordingly.
    
    5. Renaming Columns for Clarity:
        qty → quantity
        sku → stock_keeping_unit
        asin → amazon_standard_identification_number
        status → courier_status
        category → product_category
    
    6. Save to Database:
        Overwrites the existing cleaned_amazon_sale_report table with this updated version.
  
4. BusinessData.py

    File Purpose
    This script performs analytical sorting and grouping operations on the cleaned Amazon dataset stored in PostgreSQL. It generates summary tables aligned with specific business requirements and saves those summaries back into the database for reporting or dashboard use.

    1. BR1: Identify Top-Selling Product Categories and Their Performance by Region
    
        Output Table: category_sales_by_state

        Steps:

        * Convert amount from string (e.g., "INR 500") to numeric float for calculations.
        * Filter only records where courier_status == 'Delivered' to focus on successful sales.
        * Group by product_category and ship_state.
    
        Aggregate:
        * total_quantity: Total units sold.
        * total_sales: Sum of revenue.
        * order_count: Number of orders.
        * Sort the grouped table by total sales in descending order.
        * Save this summary as a new table in the database: category_sales_by_state.
    
    2.  BR2: Evaluate Order Delivery Performance by Fulfillment Type and Courier Status
    
        Output Table: delivery_performance_data

        Steps:

        * Select key columns: date, order_id, fulfilment, courier_status.
        * Sort the records by fulfilment and courier_status for easier analysis of delivery behavior by fulfillment type.
        * Save the sorted subset to the database: delivery_performance_data.

    3. BR3: Identify Regional Trends and Customer Types
        
        Output Table: regional_trends_customer_types

        Steps:

        Select relevant columns:
        * Shipping location: ship_city, ship_state, ship_country
        * Customer type: b2b
        * Financial: amount
        * Product: product_category
        * Convert amount to float (removing currency text like "INR").
        * Sort the data by ship_state and b2b to observe regional and customer-type patterns.
        * Save the result to the database: regional_trends_customer_types.




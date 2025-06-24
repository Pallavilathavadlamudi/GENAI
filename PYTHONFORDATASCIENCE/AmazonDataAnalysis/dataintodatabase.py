import pandas as pd
from sqlalchemy import create_engine

# 1. Load CSV
df = pd.read_csv("/Users/pallavilathavadlamudi/Desktop/Python/Amazondata/Amazon Sale Report.csv", low_memory=False)

# 2. PostgreSQL connection (with URL-encoded password)
engine = create_engine('postgresql://admin:Admin%40043@localhost:5432/ecommerce')

# 3. Upload to PostgreSQL
df.to_sql("amazon_sale_report", engine, if_exists="replace", index=False)

print(" CSV uploaded to PostgreSQL successfully!")




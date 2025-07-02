### What is **Data Extraction**?

**Data Extraction** is the process of **retrieving raw data** from various sources so that it can be analyzed, transformed, or loaded into systems like databases, dashboards, or data science tools.

###  **How Can We Extract Data?**

Here are the **main methods** used in data extraction:

### 1. **From Files**

**Examples**: Excel, CSV, JSON, XML
Tools:

* **Python**: `pandas.read_csv()`, `read_excel()`
* **Excel**: Power Query
* **R**: `read.csv()`, `readxl`

```python
import pandas as pd
data = pd.read_csv("sales_data.csv")
```

### 2. **From Databases (SQL)**

**Examples**: MySQL, PostgreSQL, SQL Server
Tools:

* SQL queries using tools like **pgAdmin**, **MySQL Workbench**
* Python with **SQLAlchemy** or **psycopg2**

```python
from sqlalchemy import create_engine
engine = create_engine('postgresql://user:pass@host:port/dbname')
data = pd.read_sql("SELECT * FROM orders", engine)
```

### 3. **From APIs (Application Programming Interfaces)**

Used when data comes from **online services** (e.g., weather, stock data, YouTube)
Tools:

* `requests` library in Python
* Tools like Postman for testing

```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json()
```

### 4. **Web Scraping**

Used to collect data from **web pages** that don’t have APIs
Tools:

* Python: `BeautifulSoup`, `Selenium`, `Scrapy`

```python
from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(requests.get("https://example.com").text, "html.parser")
```

### 5. **From Cloud Platforms**

 **Examples**: AWS S3, Google BigQuery, Azure
Tools:

* Python SDKs (`boto3` for AWS, `google-cloud-bigquery`)
* Cloud-native connectors (e.g., Power BI or Tableau connectors)

### 6. **From Logs, Sensors, or IoT Devices**

Raw data from devices, stored in formats like `.log` or streamed real-time
Tools:

* Kafka, Flume (real-time pipelines)
* Python: parsing text files

###  Summary:

| Source             | Tools                      | Use Case                    |
| ------------------ | -------------------------- | --------------------------- |
| Files (CSV, Excel) | pandas, Excel, Power Query | Local storage               |
| SQL Databases      | SQLAlchemy, psycopg2, JDBC | Enterprise or app databases |
| APIs               | requests, Postman          | Web services, real-time     |
| Web Scraping       | BeautifulSoup, Selenium    | No API access               |
| Cloud Platforms    | AWS/GCP SDKs, BI tools     | Big data, remote sources    |
| Logs/Sensors       | Kafka, Spark, Python       | IoT or log monitoring       |

>  **Data Extraction** is the **first step** in the ETL (Extract, Transform, Load) pipeline — and it's essential to access quality data before analysis or modeling.

## **Types of Data**

Data can be categorized in several ways, but the most common classifications are:

### 1. **Structured Data**

* Data that is organized into **tables**, **rows**, and **columns**
* Easily stored in **relational databases** like SQL
* Examples:

  * Sales records
  * Employee database
  * Bank transactions

*Easy to search and analyze using SQL or spreadsheets*

### 2. **Unstructured Data**

* Data with **no fixed format or schema**
* Harder to organize and analyze directly
* Examples:

  * Text (emails, reviews, social media posts)
  * Images, videos, audio files
  * Scanned documents

*Requires advanced tools like NLP or image processing to analyze*

### 3. **Semi-Structured Data**

* Data that **has some structure** but not in a traditional table format
* Often stored in formats like **JSON, XML, NoSQL**
* Examples:

  * Sensor logs
  * API responses
  * Web scraping output

*Has labels or tags but not strictly tabular*

---

## **Raw Data vs. Processed Data**

| Feature            | **Raw Data**                                                      | **Processed Data**                                             |
| ------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------- |
| **Definition**     | Data collected **directly from source** with **no modifications** | Data that has been **cleaned, formatted, and transformed**     |
| **Structure**      | Often messy, unorganized                                          | Well-structured and analysis-ready                             |
| **Examples**       | - Log files<br>- Sensor readings<br>- Survey responses as-is      | - Cleaned CSV file<br>- Database table<br>- Summary statistics |
| **Use Case**       | Initial capture for storage                                       | Used in analysis, dashboards, or ML                            |
| **Tools Required** | May need special parsing or scripting                             | Ready for Excel, SQL, or ML models                             |
| **Quality**        | May include errors, noise, duplicates                             | High-quality and consistent                                    |

###  In simple terms:

* **Raw Data** = Uncooked ingredients
* **Processed Data** = Prepared dish, ready to eat (or analyze)

## **Labeled Data and Unlabeled Data**

### **Labeled Data**

**Definition:**
Data that includes both the input and the correct output (label).

**Example:**

* Text: "Great product!" → Label: *Positive*
* Image: \[Picture of a cat] → Label: *Cat*

### **Unlabeled Data**

**Definition:**
Data that includes only the input, without any known labels or outcomes.

**Example:**

* Text: "Great product!" → No label
* Image: \[Picture of a cat] → No label

### What is **Data Wrangling**?

**Data Wrangling**, also known as **Data Munging**, is the process of **cleaning, transforming, and preparing raw data** into a usable format for analysis or modeling.

It is a **critical early step** in the data science pipeline — before you can analyze or model the data, you must ensure it's clean, structured, and meaningful.

### Key Steps in Data Wrangling:

1. **Data Collection**

   * Import data from sources: CSV, databases, APIs, etc.

2. **Data Cleaning**

   * Handle **missing values**
   * Fix **inconsistent formatting** (e.g., date formats)
   * Remove **duplicates** or irrelevant entries

3. **Data Transformation**

   * Convert data types (e.g., strings to dates)
   * Normalize or scale numerical values
   * Extract or create new features (columns)

4. **Data Integration**

   * Merge data from multiple sources or tables

5. **Data Validation**

   * Check for outliers, logic errors, or incorrect values

6. **Data Structuring**

   * Reshape data into tidy format (e.g., pivot tables)
   * Ensure the structure matches modeling or analysis needs

### Example:

You receive a dataset with:

* Missing product prices
* "Date" column as text
* City names in inconsistent cases
* Duplicated order records

**Data wrangling** would involve:

* Filling in or removing missing prices
* Converting "Date" to datetime format
* Standardizing city names (e.g., "new york", "New York")
* Removing duplicates

### Why is Data Wrangling Important?

* Ensures **data quality** and **reliability**
* Saves time later in modeling and visualization
* Prevents errors and misleading results

###  Tools Commonly Used:

* **Python**: pandas, NumPy
* **R**: dplyr, tidyr
* **Excel/Power Query**
* **SQL**: for joining and filtering data
* **Power BI / Tableau Prep**: for visual wrangling

> **In short:**
> **Data Wrangling = Turning messy data into clean, structured, and usable data.**
> It's like preparing ingredients before cooking — essential for a good outcome.

Great question! While **Data Wrangling** and **Data Cleaning** are closely related (and often overlap), they are **not exactly the same**. Here's a clear comparison to help you understand the difference:

### **Data Wrangling vs. Data Cleaning**

| Feature             | **Data Cleaning**                                                                     | **Data Wrangling**                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**      | The process of **removing or fixing incorrect, incomplete, or inaccurate data**       | The broader process of **transforming raw data into a usable format**, including cleaning, reshaping, and integrating               |
| **Scope**           | A **subset** of data wrangling                                                        | A **wider process** that includes cleaning + other transformation steps                                                             |
| **Focus**           | Accuracy and consistency of data                                                      | Structuring, reshaping, enriching, and integrating data                                                                             |
| **Typical Tasks**   | - Handle missing values<br>- Remove duplicates<br>- Correct typos<br>- Fix data types | - Data cleaning tasks **plus**:<br>- Merge datasets<br>- Create new features<br>- Normalize values<br>- Reshape tables (pivot/melt) |
| **When It Happens** | Often early in the data workflow                                                      | Throughout the **entire preprocessing stage**                                                                                       |
| **End Goal**        | Get **error-free** data                                                               | Get **structured and analysis-ready** data                                                                                          |

### Think of it this way:

* **Data Cleaning** = Making sure the data is **correct and consistent**
* **Data Wrangling** = Making the data **correct + usable + well-structured**

### Example:

You receive a dataset:

* Some rows have missing “Amount”
* The “Date” column is in text format
* Two tables (orders and products) need to be merged

**Data Cleaning** would:

* Fill or drop missing "Amount"
* Convert "Date" to datetime
* Remove duplicates

**Data Wrangling** would:

* Do all the above cleaning
* Merge tables
* Add a new column: "Amount after Discount"
* Normalize product names
* Reshape data to group by category

### Summary:

> **Data Cleaning is a part of Data Wrangling.**
> You **clean** the data to remove problems, and then you **wrangle** it to make it useful for analysis or modeling.


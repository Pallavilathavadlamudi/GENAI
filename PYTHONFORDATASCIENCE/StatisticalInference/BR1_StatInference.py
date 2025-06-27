import math
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_ind
from scipy.stats import norm, beta


#1. the table is created and saved from BusinessData.py
#BR:1 Identify top-selling product categories and their performance by region. (Category_sales_by_state)

engine = create_engine('postgresql://admin:Admin%40043@localhost:5432/ecommerce')

#3. Read data from PostgreSQL
Amazondata = pd.read_sql("SELECT * FROM category_sales_by_state",engine)

# 4. Schema of the data
Amazondataschema = pd.DataFrame({
    'Column Name': Amazondata.columns,
    'Data Type': Amazondata.dtypes.values,
    'Missing Values': Amazondata.isnull().sum().values,
    'Unique Values': Amazondata.nunique().values,
})

print("\nDataset Schema Summary:")
print(Amazondataschema)

# Optional: View head, tail, describe separately
print("\nHead of the dataset:")
print(Amazondata.head())

print("\nTail of the dataset:")
print(Amazondata.tail())

print("\nDescriptive statistics:")
print(Amazondata.describe())

'''
You want to analyze:

Which product categories sell best (e.g., "Set", "Kurta", "Western Dress", etc.)
Where they sell best (state-wise performance)
Using cleaned and filtered data (e.g., only successful deliveries)
Let’s now map each probability/inference/statistical concept to your task '''

#1) “What’s the probability that a Kurta ordered from Karnataka is among the top 10 selling category-state pairs?

# Correct way to calculate the true probability in the whole dataset
prob = len(Amazondata[(Amazondata['product_category'] == 'kurta') & 
                      (Amazondata['ship_state'] == 'Karnataka')]) / len(Amazondata)

print(f"Probability: {prob:.4f}")

    # 1. Probability

# What’s the probability that a randomly selected row 
# (i.e., a product-category + state pair) is one of the top 3 categories by total sales?

# Step 1: Total sales per product category
category_sales = Amazondata.groupby('product_category')['total_sales'].sum()
print("\nTotal Sales by Product Category:")
print(category_sales.sort_values(ascending=False))  # Optional: sorted for better readability

# Step 2: Identify top 3 categories
top_categories = category_sales.nlargest(3).index.tolist()
print("\nTop 3 Product Categories by Total Sales:")
print(top_categories)

# Step 3: Filter rows that belong to those categories
top_category_rows = Amazondata[Amazondata['product_category'].isin(top_categories)]
count_top_category_rows = len(top_category_rows)
print(f"\nNumber of Records Belonging to Top 3 Categories: {count_top_category_rows}")

# Step 4: Compute probability
total_rows = len(Amazondata)
prob_top_categories = count_top_category_rows / total_rows
print(f"\nTotal Records in Dataset: {total_rows}")
print(f"Probability that a record is from a Top 3 Category: {prob_top_categories:.3f}")

    #2. Estiamate Samples

#1. Select the column you want to analyze
sales_data = Amazondata['total_sales']

#2. Calculate the Point Estimate (Mean)
point_estimate = sales_data.mean()

#3. Set the Confidence Level
confidence_level = 0.95

#4. Calculate the Standard Error (SE)
n = len(sales_data)
sample_std = np.std(sales_data, ddof=1)  # Sample standard deviation
standard_error = sample_std / math.sqrt(n)

#5.Find the t-critical value
t_critical = stats.t.ppf((1 + confidence_level) / 2, df=n-1)

#6. Calculate Margin of Error
margin_of_error = t_critical * standard_error

#7. Compute the Confidence Interval
lower_bound = point_estimate - margin_of_error
upper_bound = point_estimate + margin_of_error
confidence_interval = (lower_bound, upper_bound)

#8. Print the Results
print(f"Point Estimate (Mean): ₹{point_estimate:.2f}")
print(f"Confidence Level: {confidence_level * 100:.0f}%")
print(f"Standard Error (SE): ₹{standard_error:.2f}")
print(f"T-Critical Value: {t_critical:.3f}")
print(f" Margin of Error: ₹{margin_of_error:.2f}")
print(f"Confidence Interval: ₹{lower_bound:.2f} to ₹{upper_bound:.2f}")

'''With a 95% confidence level, the true average total sales is likely within ₹22,213 of our sample mean (₹70,828).'''

    # 3. Normal Distribution and Bayes' Inference

'''PDF & CDF → How your overall sales are distributed.
Bayesian Inference → Do the actual data support your belief that “kurta” is a leading category?'''

# 1. Normal Distribution - Total Sales

sales = Amazondata['total_sales']
mean = sales.mean()
std = sales.std()
x_sales = np.linspace(sales.min(), sales.max(), 1000)

plt.plot(x_sales, norm.pdf(x_sales, mean, std))
plt.title("PDF - Total Sales Distribution")
plt.xlabel("Total Sales")
plt.ylabel("Density")
plt.grid()
plt.show()

plt.plot(x_sales, norm.cdf(x_sales, mean, std))
plt.title("CDF - Total Sales Distribution")
plt.xlabel("Total Sales")
plt.ylabel("Cumulative Probability")
plt.grid()
plt.show()

# 2. Bayesian Inference - 'kurta' as Top Category

# Step 1: Prior belief using Beta distribution (60% belief)
prior_alpha = 6
prior_beta = 4

# Step 2: Observed data - count how many rows have 'kurta' as category
is_kurta = Amazondata['product_category'].str.lower() == 'kurta'
successes = is_kurta.sum()
trials = len(Amazondata)

# Step 3: Posterior update
posterior_alpha = prior_alpha + successes
posterior_beta = prior_beta + (trials - successes)

# Step 4: Plot Prior vs Posterior
x_beta = np.linspace(0, 1, 1000)
prior_dist = beta(prior_alpha, prior_beta)
posterior_dist = beta(posterior_alpha, posterior_beta)

plt.plot(x_beta, prior_dist.pdf(x_beta), label='Prior: Belief before data (60%)', linestyle='--')
plt.plot(x_beta, posterior_dist.pdf(x_beta), label='Posterior: Updated after data', linewidth=2)
plt.axvline(successes / trials, color='gray', linestyle=':', label='Observed Proportion')

plt.title("Bayesian Inference: Likelihood 'kurta' is Top Category")
plt.xlabel("Probability")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()

# Hypothesis Testing
# Are the average sales for "kurta" different from other categories?

# Separate sales data
kurta_sales = Amazondata[Amazondata['product_category'].str.lower() == 'kurta']['total_sales']
other_sales = Amazondata[Amazondata['product_category'].str.lower() != 'kurta']['total_sales']

# Summary stats
print("\nDescriptive Statistics")
print(f"Kurta mean sales: {kurta_sales.mean():,.2f}")
print(f"Other categories mean sales: {other_sales.mean():,.2f}\n")

# Perform two-sample t-test (Welch's t-test, no equal variance assumption)
t_stat, p_value = ttest_ind(kurta_sales, other_sales, equal_var=False)

print("\nHypothesis Testing Results")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Decision based on p-value
alpha = 0.05
if p_value < alpha:
    print("✅ Reject the null hypothesis: Significant difference in average sales.")
else:
    print("❌ Fail to reject the null hypothesis: No significant difference.")

# Example: Select two similar categories, e.g., "kurta" vs "Western Dress"

# Filter two similar product categories
category_1 = 'kurta'
category_2 = 'Saree'

sales_1 = Amazondata[Amazondata['product_category'].str.lower() == category_1.lower()]['total_sales']
sales_2 = Amazondata[Amazondata['product_category'].str.lower() == category_2.lower()]['total_sales']

# Print their mean sales
print("\nDescriptive Analysis:")
print(f"Mean Sales - {category_1}: ₹{sales_1.mean():,.2f}")
print(f"Mean Sales - {category_2}: ₹{sales_2.mean():,.2f}")

# Perform t-test
t_stat, p_value = ttest_ind(sales_1, sales_2, equal_var=False)

# Results
print("\nHypothesis Test Result")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("✅ Reject the null hypothesis: Significant difference.")
else:
    print("❌ Fail to reject the null hypothesis: No significant difference. Null hypothesis likely true.")

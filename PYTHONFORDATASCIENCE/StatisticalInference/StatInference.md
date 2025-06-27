##  **1. Data Loading and Preparation**

* Connecting to a **PostgreSQL database** that contains a table named `category_sales_by_state`.
* Reading the data into a Pandas DataFrame.
* Displaying a **schema summary** that includes:

  * Column names
  * Data types (e.g., int, float, object)
  * Number of missing values
  * Count of unique values

This step ensures your dataset is clean and ready for analysis.

## **2. Exploratory Data Analysis (EDA)**

You preview the first and last few rows of data and generate summary statistics (like count, mean, std, min, max). This helps you:

* Understand the distribution of sales and orders
* Spot any anomalies or patterns in the dataset

**business requirement**:

> "Identify top-selling product categories and their performance by region."

## **3. Probability Calculations**

two probability-based business questions:

### a. **Probability of a Specific Event**

> *“What is the probability that a 'kurta' ordered from Karnataka appears in the dataset?”*

You compute this by dividing the number of matching records by the total number of records. It gives you the **likelihood** of that specific product-state combination occurring.

### b. **Probability of Top Categories**

> *“What’s the probability that a randomly selected record belongs to the top 3 product categories by total sales?”*

* Rank product categories by total sales.
* Find the top 3.
* Calculate what portion of the dataset belongs to those categories.

This gives insight into how dominant your top sellers are in the overall business.

## **4. Statistical Estimation (Confidence Intervals)**

Here, you compute a **confidence interval** for the average total sales across all products and regions. This includes:

* **Point Estimate**: The sample mean (i.e., average total sales).
* **Standard Error**: How much the sample mean might vary if you took multiple samples.
* **T-Critical Value**: From the t-distribution, based on your confidence level (95%).
* **Margin of Error**: The range within which the true mean likely falls.

You then calculate the **confidence interval**, which tells you:

> *“We are 95% confident that the true average total sales lies between ₹X and ₹Y.”*

This is helpful for **sales forecasting** and **business planning**.

## **5. Normal Distribution Analysis**

You assume that total sales follow a **normal (bell-shaped) distribution** and visualize this using:

* **PDF (Probability Density Function)**: Shows the **likelihood** of different sales values.
* **CDF (Cumulative Distribution Function)**: Shows the **probability** that sales are **less than or equal to** a certain value.

This helps you understand the **spread and concentration** of sales data — crucial for predicting outcomes and making inventory decisions.

## **6. Bayesian Inference**

You apply **Bayes' Theorem** to evaluate:

> *“How likely is it that 'kurta' is a top-selling category?”*

### You follow these steps:

* **Prior Belief**: You assume a 60% chance that 'kurta' is a top category.
* **Observed Data**: You count how often 'kurta' appears in the dataset.
* **Posterior Belief**: You update your prior belief using actual data.

You then plot:

* The **prior distribution** (before seeing the data)
* The **posterior distribution** (after seeing the data)
* The **observed proportion**

This Bayesian analysis allows you to **refine your assumptions** using real evidence.

## **7. Hypothesis Testing (t-tests)**

You perform **Welch’s t-test** to compare average sales between product categories.

### a. **Kurta vs All Other Categories**

* **Null Hypothesis (H₀)**: Kurta has the same average sales as other categories.
* **Alternative Hypothesis (H₁)**: Kurta has different average sales.
* If the p-value is **less than 0.05**, you reject H₀ (significant difference).
* If the p-value is **greater than 0.05**, you fail to reject H₀ (no significant difference).

### b. **Kurta vs Saree** (Example where H₀ holds)

This test shows:

> Even if two categories have different averages, the **difference might not be statistically significant** — meaning the difference could be due to chance.

This demonstrates how hypothesis testing helps **validate patterns** rather than just rely on visual or mean differences.

## Final Outcome

**statistical analysis pipeline**:

* It estimates **probabilities**
* Calculates **confidence intervals**
* Visualizes **normal distribution**
* Applies **Bayesian reasoning**
* Tests **hypotheses**

Each technique adds a **layer of insight** to your business question:
**"Which categories are truly top-performing, and where?"**



## **Feature Transformation**

### **Definition**:

Feature transformation is the process of **modifying existing features** to improve their **scale**, **distribution**, or **format** so that they become **more suitable for machine learning models**.

---

##  **Why Feature Transformation?**

* ML models often assume certain **data characteristics** (e.g., normal distribution, no missing values).
* Untransformed features can lead to:

  * Poor predictions
  * Long training time
  * Model bias due to outliers or categorical misinterpretation

---

## Common Feature Transformation Techniques

Here's a breakdown of the key transformation tasks and their purposes:

| **Task**                 | **Purpose**                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| **1. Imputation**        | Fill in missing values to prevent information loss or model errors          |
| **2. Outlier Handling**  | Prevent extreme values from distorting model training                       |
| **3. Binning**           | Convert continuous variables into discrete intervals (bins)                 |
| **4. Log Transform**     | Normalize right-skewed data (e.g., income, prices)                          |
| **5. One-Hot Encoding**  | Convert categorical variables into numeric binary columns                   |
| **6. Feature Splitting** | Split compound features (like full address or datetime) into multiple parts |
| **7. Scaling**           | Normalize numerical feature ranges for fair comparison                      |

---

## Detailed Explanation & Examples

### **Imputation**

> Fill in missing data with suitable values.

```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
df['age'] = imputer.fit_transform(df[['age']])
```

---

### **Outlier Handling**

> Remove or cap extreme values.

```python
# Remove values beyond 1.5*IQR
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['salary'] >= Q1 - 1.5 * IQR) & (df['salary'] <= Q3 + 1.5 * IQR)]
```

---

### **Binning**

> Convert continuous features into categories.

```python
df['age_bin'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100], labels=['Teen', 'Adult', 'MidAge', 'Senior'])
```

---

###  **Log Transformation**

> Handle skewed distributions (e.g., sales amounts).

```python
import numpy as np
df['log_sales'] = np.log1p(df['sales'])  # log1p avoids issues with log(0)
```

---

### **One-Hot Encoding**

> Convert categories into binary columns.

```python
df = pd.get_dummies(df, columns=['product_category'])
```

---

### **Feature Splitting**

> Extract new features from compound ones (e.g., dates or text).

```python
df['purchase_date'] = pd.to_datetime(df['purchase_date'])
df['purchase_month'] = df['purchase_date'].dt.month
df['purchase_day'] = df['purchase_date'].dt.day
```

---

###  **Scaling**

> Normalize feature ranges (important for algorithms like KNN, SVM, logistic regression).

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['income', 'expenses']] = scaler.fit_transform(df[['income', 'expenses']])
```

---

## Bonus: When is Each Method Important?

| **Transformation**   | **When to Use**                                                          |
| -------------------- | ------------------------------------------------------------------------ |
| **Imputation**       | When you have missing data                                               |
| **Outlier Handling** | When data contains rare/extreme values (skewed influence)                |
| **Binning**          | When you want to simplify numerical variables or use rule-based modeling |
| **Log Transform**    | When numerical data is heavily skewed (e.g., exponential distributions)  |
| **Encoding**         | When working with categorical variables                                  |
| **Splitting**        | When compound columns contain multiple pieces of useful data             |
| **Scaling**          | When features have different units or value ranges                       |

---

## Summary

| Step              | Goal                                   | Example                         |
| ----------------- | -------------------------------------- | ------------------------------- |
| Imputation        | Fill missing values                    | Replace NaNs in `age` with mean |
| Outlier Handling  | Reduce skew from rare/extreme values   | Remove salary > 3×IQR           |
| Binning           | Simplify ranges                        | Convert `age` to groups         |
| Log Transform     | Normalize skewed distributions         | Log of `sales`                  |
| One-Hot Encoding  | Convert categorical → numeric          | `shirt` → \[1, 0, 0]            |
| Feature Splitting | Derive new features from compound data | `2024-06-13` → month=6, day=13  |
| Scaling           | Standardize feature ranges             | Income scaled to mean=0, std=1  |


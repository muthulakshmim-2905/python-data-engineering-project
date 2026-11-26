import pandas as pd
import numpy as np

# Step 1: Load Cleaned Dataset

df = pd.read_csv("employee_data.csv")

print("CLEANED DATASET")
print(df.head())


# Step 2: Summary Statistics

print("\nSUMMARY STATISTICS")

print("Mean:")
print(df[["Age", "Salary"]].mean())

print("Median:")
print(df[["Age", "Salary"]].median())

print("Minimum:")
print(df[["Age", "Salary"]].min())

print("Maximum:")
print(df[["Age", "Salary"]].max())

print("Standard Deviation:")
print(df[["Age", "Salary"]].std())


# Step 3: Department Groupby Analysis

print("\nDEPARTMENT ANALYSIS")

department_analysis = df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Age": "mean"
})

print(department_analysis)


# Step 4: City Groupby Analysis

print("\nCITY ANALYSIS")

city_analysis = df.groupby("City").agg({
    "Salary": "mean",
    "Age": "mean"
})

print(city_analysis)


# Step 5: Gender Groupby Analysis

print("\nGENDER ANALYSIS")

gender_analysis = df.groupby("Gender").agg({
    "Salary": "mean",
    "Age": "mean"
})

print(gender_analysis)


# Step 6: Correlation Analysis

print("\nCORRELATION MATRIX")

correlation = df.corr(numeric_only=True)

print(correlation)


# Find Top 3 Correlation Relationships

corr_pairs = correlation.where(
    np.triu(np.ones(correlation.shape), k=1).astype(bool)
).stack()

top_3 = corr_pairs.reindex(
    corr_pairs.abs().sort_values(ascending=False).index
).head(3)

print("\nTOP 3 CORRELATION RELATIONSHIPS")
print(top_3)


# Step 7: Business Questions

print("\nBUSINESS QUESTIONS")

# Question 1
print("\n1. Which department has highest average salary?")

print(df.groupby("Department")["Salary"].mean().idxmax())


# Question 2
print("\n2. What is the average employee salary?")

print(df["Salary"].mean())


# Question 3
print("\n3. Which city has highest number of employees?")

print(df["City"].value_counts().idxmax())


# Question 4
print("\n4. Which gender has highest average salary?")

print(df.groupby("Gender")["Salary"].mean())


# Question 5
print("\n5. What is the maximum employee salary?")

print(df["Salary"].max())


# Step 8: Merge Department Budget

print("\nMERGE DEPARTMENT BUDGET")

budget = pd.DataFrame({
    "Department": ["It", "Hr", "Sales", "Finance"],
    "Budget": [500000, 300000, 600000, 400000]
})

merged_data = pd.merge(
    df,
    budget,
    on="Department",
    how="left"
)

print(merged_data)


# Step 9: Bonus - Pivot Table

print("\nPIVOT TABLE")

pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print(pivot)


# Step 10: Save EDA Output

merged_data.to_csv("EDA_Output.csv", index=False)

print("\nEDA COMPLETED SUCCESSFULLY!")

print("EDA Output Saved Successfully!")
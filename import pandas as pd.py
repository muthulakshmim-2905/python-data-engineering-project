import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load Dataset

df = pd.read_csv("employee_data.csv")

# Create folder to save charts

os.makedirs("reports/figures", exist_ok=True)


# Chart 1: Bar Chart

avg_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8, 5))

avg_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend(["Average Salary"])

plt.tight_layout()
plt.savefig("reports/figures/bar_chart.png")
plt.show()

print("Insight: Average salary differs across departments.")


# Chart 2: Histogram

plt.figure(figsize=(8, 5))

plt.hist(df["Salary"], bins=10, color="green",
         edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("reports/figures/histogram.png")
plt.show()

print("Insight: The histogram shows the distribution of employee salaries.")


# Chart 3: Scatter Plot

plt.figure(figsize=(8, 5))

plt.scatter(df["Age"], df["Salary"],
            color="red", label="Employees")

plt.title("Age vs Salary")
plt.xlabel("Age (Years)")
plt.ylabel("Salary (INR)")
plt.legend()

plt.tight_layout()
plt.savefig("reports/figures/scatter_plot.png")
plt.show()

print("Insight: The scatter plot shows the relationship between age and salary.")


# Chart 4: Line Chart

sorted_salary = df["Salary"].sort_values().reset_index(drop=True)

plt.figure(figsize=(8, 5))

plt.plot(sorted_salary, color="purple",
         label="Salary")

plt.title("Sorted Employee Salary")
plt.xlabel("Employee Rank (Sorted)")
plt.ylabel("Salary (INR)")
plt.legend()

plt.tight_layout()
plt.savefig("reports/figures/line_chart.png")
plt.show()

print("Insight: Salaries are displayed in ascending order.")


# Chart 5: Heatmap

correlation = df.corr(numeric_only=True)

plt.figure(figsize=(8, 5))

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar(label="Correlation")

plt.xticks(range(len(correlation.columns)),
           correlation.columns, rotation=45)

plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Employee Data Correlation Heatmap")
plt.xlabel("Variables")
plt.ylabel("Variables")

plt.tight_layout()
plt.savefig("reports/figures/heatmap.png")
plt.show()

print("Insight: The heatmap shows correlations between numerical variables.")

print("\nALL 5 CHARTS CREATED SUCCESSFULLY!")
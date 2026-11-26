import matplotlib.pyplot as plt

salary = [18000, 22000, 25000, 28000, 30000,
          35000, 38000, 40000, 45000, 50000]

plt.figure(figsize=(8,5))

plt.boxplot(salary)

plt.title("Salary Distribution - Box Plot")
plt.xlabel("Employees")
plt.ylabel("Salary (₹)")

plt.savefig("reports/figures/box_plot.png")

plt.show()
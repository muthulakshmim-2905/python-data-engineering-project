import matplotlib.pyplot as plt

age = [22, 25, 28, 30, 32, 35, 38, 40]

salary = [18000, 22000, 28000, 30000,
          35000, 40000, 45000, 50000]

plt.figure(figsize=(8,5))

plt.scatter(age, salary, marker="o")

plt.title("Age vs Salary")
plt.xlabel("Age (Years)")
plt.ylabel("Salary (₹)")

plt.savefig("reports/figures/scatter_plot.png")

plt.show()
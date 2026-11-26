import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [10000, 15000, 12000, 20000, 25000, 30000]

plt.figure(figsize=(8,5))

plt.plot(months, sales, marker="o", linestyle="-")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

plt.savefig("reports/figures/line_chart.png")

plt.show()
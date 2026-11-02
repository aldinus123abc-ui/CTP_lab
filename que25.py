import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

max_month = months[sales.index(max(sales))]
min_month = months[sales.index(min(sales))]
print("Highest sales:", max_month, max(sales))
print("Lowest sales:", min_month, min(sales))

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(months, sales, color='skyblue')
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.show()
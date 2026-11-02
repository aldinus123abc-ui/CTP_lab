import matplotlib.pyplot as plt

hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(hours, bins=5, color='skyblue', edgecolor='black')
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours/Week")
plt.ylabel("Number of Students")

plt.subplot(1, 2, 2)
plt.hist(scores, bins=5, color='lightgreen', edgecolor='black')
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()

plt.scatter(hours, scores, color='purple')
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours/Week")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()
import numpy as np

students = np.array(['S1', 'S2', 'S3', 'S4', 'S5'])
subjects = np.array(['Mathematics', 'Physics', 'Chemistry', 'English'])


mid_sem = np.array([
    [65, 70, 68, 72],
    [78, 75, 80, 77],
    [55, 60, 58, 62],
    [82, 85, 80, 88],
    [70, 68, 72, 74]
])


end_sem = np.array([
    [72, 78, 75, 80],
    [84, 82, 86, 83],
    [65, 68, 66, 70],
    [88, 90, 85, 92],
    [78, 75, 80, 82]
])


mid_total = np.sum(mid_sem, axis=1)
end_total = np.sum(end_sem, axis=1)


mid_avg = np.mean(mid_sem, axis=1)
end_avg = np.mean(end_sem, axis=1)

percentage_improvement = ((end_total - mid_total) / mid_total) * 100

print(f"{'Student':<10} | {'Mid Total':<10} | {'End Total':<10} | {'Mid Avg':<10} | {'End Avg':<10} | {'Improvement (%)':<15}")
print("-" * 75)

for i in range(len(students)):
    print(f"{students[i]:<10} | {mid_total[i]:<10} | {end_total[i]:<10} | {mid_avg[i]:<10.2f} | {end_avg[i]:<10.2f} | {percentage_improvement[i]:<15.2f}%")
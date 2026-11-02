import numpy as np
import statistics

datasets = {
    "Marks": [78, 85, 92, 67, 88, 73, 95, 81, 76, 89],
    "Temperatures": [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5],
    "Sales": [12500, 13800, 14200, 11900, 15100, 14750, 16000]
}

print(f"{'Dataset':<15} | {'Method':<12} | {'Mean':<10} | {'Median':<10} | {'Std Dev':<10} | {'Min':<10} | {'Max':<10}")
print("-" * 85)

for name, data in datasets.items():
    np_data = np.array(data)
    np_mean = np.mean(np_data)
    np_median = np.median(np_data)
    np_std = np.std(np_data, ddof=0)
    np_min = np.min(np_data)
    np_max = np.max(np_data)
    
    print(f"{name:<15} | {'NumPy':<12} | {np_mean:<10.2f} | {np_median:<10.2f} | {np_std:<10.2f} | {np_min:<10} | {np_max:<10}")

    py_mean = sum(data) / len(data)
    py_median = statistics.median(data)
    py_std = statistics.pstdev(data)  
    py_min = min(data)
    py_max = max(data)
    
    print(f"{'':<15} | {'Pure Python':<12} | {py_mean:<10.2f} | {py_median:<10.2f} | {py_std:<10.2f} | {py_min:<10} | {py_max:<10}")
    print("-" * 85)
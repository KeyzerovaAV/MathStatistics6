import numpy as np
import scipy.stats as stats

weight_before = np.array([92.8, 95.6, 92.1, 100.6, 96.2, 92.1, 96.7, 97.6, 97.0, 93.9])
weight_after = np.array([87.1, 84.1, 81.3, 77.0, 86.0, 82.9, 83.0, 85.5, 85.2, 84.6])

print(stats.ttest_rel(weight_before, weight_after, alternative = 'greater'))
print(stats.ttest_rel(weight_before, weight_after, alternative = 'less'))
print(stats.ttest_rel(weight_before, weight_after, alternative = 'two-sided'))
print(stats.ttest_rel(weight_before, weight_after))

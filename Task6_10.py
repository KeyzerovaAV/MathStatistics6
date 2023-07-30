import numpy as np
import scipy.stats as stats

p1 = 75 / 100
p2 = 69 / 100
P = (75 + 69) / (100 + 100)
delta = p1 - p2
SE = np.sqrt(P * (1 - P) * (1 / 100 + 1 / 100))
Z = stats.norm.ppf(1 - 0.05 / 2)

print(delta - Z * SE, delta + Z * SE)

# поскольку доверительный интервал проходит через 0, можно сделать вывод, 
# что улучшения в двух группах не имеют статистически значимых различий

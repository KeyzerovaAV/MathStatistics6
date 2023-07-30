import numpy as np
import scipy.stats as stats

soccer_players_height = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players_height = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weight_lifters_height = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

print(stats.shapiro(soccer_players_height))
print(stats.shapiro(hockey_players_height))
print(stats.shapiro(weight_lifters_height))
# значения всех трех групп следуют нормальному распределению

print(stats.bartlett(soccer_players_height, hockey_players_height, weight_lifters_height))
# получаем однородность (равенство) дисперсий

print(stats.f_oneway(soccer_players_height, hockey_players_height, weight_lifters_height))
# если выбираем уровень статистической значимости = 0.05, то принимаем альтернативную гипотезу, 
# т.е. делаем вывод, что статистически значимые различия среднего роста между тремя группами есть

print(stats.tukey_hsd(soccer_players_height, hockey_players_height, weight_lifters_height))
# статистически значимые различия среднего роста обнаружены 
# между футболистами и штангистами и между хоккеистами и штангистами

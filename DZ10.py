import scipy
import pandas
import numpy
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# 1) Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

football_players = [173, 175, 180, 178, 177, 185, 183, 182]
hockey_players = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifters = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]

print(scipy.stats.shapiro(football_players))
print(scipy.stats.shapiro(hockey_players))
print(scipy.stats.shapiro(weightlifters))
print("pvalue у трех выборок больше alfa (0.05), соответственно распределение нормальное")

print(scipy.stats.bartlett(football_players, hockey_players, weightlifters))

print(scipy.stats.f_oneway(football_players, hockey_players, weightlifters), "различия роста статистически значимые")

df = pandas.DataFrame({'score': [173, 175, 180, 178, 177, 185, 183, 182, 179.125, 179.125, 179.125, \
    177, 179, 180, 188, 177, 172, 171, 184, 180, 178.67, 178.67, \
        172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170],\
            'group': numpy.repeat(['football_players', 'hockey_players', 'weightlifters'], repeats= 11 )})
tukey = pairwise_tukeyhsd(endog=df['score'], groups=df['group'], alpha=0.05)
print(tukey)
print("между футболистами и штангистами, а также между хокеистами и штангистами обнаружены статистически значимые различия в росте")
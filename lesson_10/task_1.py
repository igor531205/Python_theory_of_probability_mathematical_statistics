# Провести дисперсионный анализ для определения того, есть ли различия
# среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты:  177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты:  172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.


import numpy
from scipy import stats
from matplotlib import pyplot


if __name__ == '__main__':

    y1 = numpy.array([173, 175, 180, 178, 177, 185, 183, 182])
    y2 = numpy.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
    y3 = numpy.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

    K = 3
    n1 = y1.size
    n2 = y2.size
    n3 = y3.size
    n = n1 + n2 + n3

    y1_mean = y1.mean()
    print(f'Средний рост футболистов: {y1_mean:.1f}')

    y2_mean = y2.mean()
    print(f'Средний рост хоккеистов: {y2_mean:.1f}')

    y3_mean = y3.mean()
    print(f'Средний рост штангистов: {y3_mean:.1f}')

    total = numpy.array([*y1, *y2, *y3])
    total_mean = total.mean()
    print(f'Средний рост общий: {total_mean:.1f}')

    S_o = numpy.sum(numpy.square(total - total_mean))
    print('Сумма квадратов отклонений наблюдений от общего среднего: '
          + f'{S_o:.1f}')

    S_f = numpy.sum(numpy.square(y1_mean - total_mean)) * n1 \
        + numpy.sum(numpy.square(y2_mean - total_mean)) * n2 \
        + numpy.sum(numpy.square(y3_mean - total_mean)) * n3
    print('Сумма квадратнов отклонений средних групповых значений от общего '
          + f'среднего: {S_f:.1f}')

    S_ost = numpy.sum(numpy.square(y1 - y1_mean)) \
        + numpy.sum(numpy.square(y2 - y2_mean)) \
        + numpy.sum(numpy.square(y3 - y3_mean))
    print(f'Остаточная сумма квадратнов отклонений: {S_ost:.1f}')

    D_f = S_f / (K - 1)
    print(f'Факторная дисперсия: {D_f:.1f}')

    D_ost = S_ost / (n - K)
    print(f'Остаточная дисперсия: {D_ost:.1f}')

    F_n = D_f / D_ost
    print(f'Критерий Фишера: {F_n:.5f}')

    F_oneway = stats.f_oneway(y1, y2, y3)
    print('Однофакторный дисперсионный анализ:')
    print(f'statistic: {F_oneway.statistic:.5f}')
    print(f'pvalue: {F_oneway.pvalue:.5f}')

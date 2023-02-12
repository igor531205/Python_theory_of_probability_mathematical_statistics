# Даны значения величины заработной платы заемщиков банка (zp) и
# значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий,
# а затем с помощью функции cov из numpy. Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и
# среднеквадратичных отклонений двух признаков, а затем с использованием функций
# из библиотек numpy и pandas.


import numpy
from matplotlib import pyplot


if __name__ == '__main__':

    zp = numpy.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
    ks = numpy.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

    pyplot.scatter(zp, ks)
    pyplot.show()

    cov = numpy.mean(zp * ks) - numpy.mean(zp) * numpy.mean(ks)
    print('Ковариация')
    print(f'{cov}\n')

    cov_numpy = numpy.cov(zp, ks, ddof=0)
    print('Ковариация numpy')
    print(f'{cov_numpy}\n')

    pirson = cov / (numpy.std(zp) * numpy.std(ks))
    print('Коэффициент корреляции Пирсона')
    print(f'{pirson}\n')

    pirson_numpy = numpy.corrcoef(zp, ks)
    print('Коэффициент корреляции Пирсона numpy')
    print(f'{pirson_numpy}\n')

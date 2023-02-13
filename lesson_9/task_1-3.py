import numpy
from matplotlib import pyplot


if __name__ == '__main__':

    zp = numpy.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
    ks = numpy.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

    # Даны значения величины заработной платы заемщиков банка (zp) и
    # значения их поведенческого кредитного скоринга (ks):
    # zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
    # ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
    # Используя математические операции, посчитать коэффициенты линейной
    # регрессии, приняв за X заработную плату (то есть, zp - признак),
    # а за y - значения скорингового балла (то есть, ks - целевая переменная).
    # Произвести расчет как с использованием intercept, так и без.

    n = ks.size
    b1 = (numpy.mean(zp * ks) - numpy.mean(zp) * numpy.mean(ks)) \
        / (numpy.mean(zp**2) - numpy.mean(zp)**2)
    print(f'Коэффициент b (значение перед признаком) = {b1}')

    b0 = numpy.mean(ks) - b1 * numpy.mean(zp)
    print(f'Коэффициент a (intercept) = {b0}')

    y_pred = b0 + b1 * zp
    print(f'Прогназируемое значение y = {y_pred}')

    mse = numpy.sum((ks - y_pred)**2) / n
    print(f'Функция потерь mse = {mse}')

    zp1 = zp.reshape(1, n)
    ks1 = ks.reshape(1, n)

    b = numpy.dot(
        numpy.dot(numpy.linalg.inv(numpy.dot(zp1, zp1.T)), zp1), ks1.T)
    print(f'Матричный метод расчета коэффициента b = {b}')

    y_pred1 = b * zp
    print(f'Прогназируемое значение y (без intercept) = {y_pred1}')

    # Посчитать коэффициент линейной регрессии при заработной плате (zp),
    # используя градиентный спуск (без intercept).

    alpha = 1e-6

    B1 = 0.1
    for i in range(10):
        B1 -= alpha * (2 / n) * numpy.sum((B1 * zp - ks) * zp)
        print("B1 = {}".format(B1))

    B1 = 0.1
    for i in range(3000):
        B1 -= alpha * (2 / n) * numpy.sum((B1 * zp - ks) * zp)
        if i % 500 == 0:
            print('iteration = {i}, B1 = {B1}, mse = {mse}'.format(
                i=i, B1=B1, mse=(numpy.sum((B1 * zp - ks) ** 2) / n)))

    y_pred2 = B1 * zp
    print(f'Прогназируемое значение y = {y_pred2}')

    print(f'Функция потерь mse = {numpy.sum((B1 * zp - ks) ** 2) / n}')

    # Произвести вычисления как в пункте 2, но с вычислением intercept.
    # Учесть, что изменение коэффициентов должно производиться на каждом
    # шаге одновременно (то есть изменение одного коэффициента не должно
    # влиять на изменение другого во время одной итерации).

    for i in range(3000):
        y_pred3 = b0 + b1 * zp
        b0 -= alpha * (2 / n) * numpy.sum((y_pred3 - ks))
        b1 -= alpha * (2 / n) * numpy.sum((y_pred3 - ks) * zp)
        if i % 100 == 0:
            print('iteration = {i}, B1 = {b1}, mse = {mse}'.format(
                i=i, b1=b1, mse=(numpy.sum((b0 + b1 * zp - ks) ** 2) / n)))

'''
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25,
65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать
среднее арифметическое, среднее квадратичное отклонение, смещенную и
несмещенную оценки дисперсий для данной выборки.
'''


import numpy


def _sum_numbers(numbers: list) -> float:
    '''Функция расчета суммы чисел в списке.
    :param array: Список чисел.
    :return: Сумма чисел в списке.
    '''
    amount = 0
    for number in numbers:
        amount += number
    return amount


def _root_mean_square(numbers: list) -> float:
    mid = mean(numbers)
    root_mean_square = 0
    for number in numbers:
        root_mean_square +=
    return


def mean(numbers: list) -> float:
    '''Функция расчета среднего арифметического.
    :param array: Список чисел.
    :return: Среднее арифметическое.
    '''
    amount = _sum_numbers(numbers)
    length = len(numbers)

    return amount / length if length else 0.0


def standard_deviation(numbers: list) -> float:
    '''Функция расчета среднего квадратичного отклонения.
    :param array: Список чисел.
    :return: Среднее квадратичное отклонение.
    '''
    (np.sum((salaries - salaries_mean)**2) / salaries.size)**0.5
    (np.sum((salaries - salaries_mean)**2) / salaries.size)**0.5
    amount = _sum_numbers(numbers)
    length = len(numbers)
    for number in numbers:
        amount += number

    return amount / length if length else 0.0


def shifted_variance(numbers: numpy.array) -> float:
    '''Функция расчета смещенной дисперсии.
    :param array: Список чисел.
    :return: Смещенная дисперсия.
    '''

    return numpy.sum((numbers - numbers.mean())**2) / numbers.size


def unbiased_variance(array: numpy.array) -> float:
    '''Функция расчета несмещенной дисперсии.
    :param array: Список чисел.    
    :return: Несмещенная дисперсия.
    '''
    return 1.0


if __name__ == '__main__':

    salary_array = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55,
                    70, 75, 65, 84, 90, 150]
    salary_array.sort()
    salary_array_np = numpy.array(salary_array)

    print('Даны значения зарплат из выборки выпускников:', *salary_array)

    print('Среднее арифметическое:', mean(salary_array))
    print('Проверка результата:', salary_array_np.mean())

    print('Проверка результатов:')


'''
    print('Смещенная дисперсия:', shifted_variance(salary_array))

    print('Несмещенная дисперсия:', unbiased_variance(salary_array))

    print(numpy.std(salary_array))
    print(numpy.std(salary_array, ddof=1))
'''

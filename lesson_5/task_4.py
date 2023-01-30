# Есть ли статистически значимые различия в росте дочерей и матерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160

import numpy
from scipy import stats


if __name__ == '__main__':

    mothers_growth = numpy.array(
        [172, 177, 158, 170, 178, 175, 164, 160, 169])

    daughters_growth = numpy.array(
        [173, 175, 162, 174, 175, 168, 155, 170, 160])

    print(stats.ttest_ind(mothers_growth, daughters_growth))

    '''print((mothers_growth.mean() - daughters_growth.mean()) / numpy.sqrt(
        mothers_growth.var(ddof=1) / mothers_growth.size
        + daughters_growth.var(ddof=1) / daughters_growth.size)
    )'''

    print('Статистически значимых различий в росте дочерей нет')

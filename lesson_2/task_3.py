from math import comb, pow


def bernoulli(k: int, n: int, p: float, q: float) -> float:
    '''Формула Бурнули.
    :param k: Число наступлений события.
    :param n: Число испытаний.
    :param p: Вероятность наступления события.
    :param q: Противоположная вероятность.
    :return: Вероятность события.
    '''
    return comb(n, k) * pow(p, k) * pow(q, (n - k))


if __name__ == '__main__':
    ''' 
    Монету подбросили 144 раза. Какова вероятность, что орел выпадет 
    ровно 70 раз?
    '''
    n = 144
    k = 70
    p = 0.5
    q = 1 - p

    print('Вероятность, что орел выпадет ровно 70 раз равна',
          f'{bernoulli(k, n, p, q):.5f}')

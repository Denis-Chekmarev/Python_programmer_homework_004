"""
Вычислить число c заданной точностью d

Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

"""

from functions import input_float_numb

def get_pi():
    pi = 3
    flag = True
    for i in range(2, 100, 2):
        if flag:
            pi += 4 / (i * (i+1) * (i+2))
            flag = False
        else:
            pi -= 4 / (i * (i+1) * (i+2))
            flag = True
    return pi


def get_count_after_comma(number: float) -> int:
    number = str(number)
    list_parts = number.split('.')
    return len(list_parts[1])


if __name__ == '__main__':
    d = input_float_numb('Input the accuracy -> ')
    while not (10**(-10) <= d <= 10**(-1)):
        d = input_float_numb('Accuracy is not correct. Try again -> ')
    pi = get_pi()
    print(f'{pi:.{get_count_after_comma(d)}f}')
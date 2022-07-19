"""
Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

"""

from functions import get_number
from functions import code_power
from random import randint as rd


def get_super_number(power: int) -> str:
    if power < 10:
        return code_power[power]
    else:
        res = ''
        for i in str(power):
            res += f'{code_power[int(i)]}'
        return res


def get_equation(k=2) -> str:
    result = ''
    for i in range(int(k), 1, -1):
        result += f'{str(rd(0,100))}x{get_super_number(i)} + '

    result += f'{str(rd(0,100))}x + {str(rd(0,100))} = 0'
    return result


def write_file(filename: str, text: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text + '\n')


k = get_number('Input k -> ')
print(get_equation(k))
write_file('004.txt', get_equation(k))
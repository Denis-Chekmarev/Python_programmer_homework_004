"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.

"""

#         0: '\u2070',
#         1: '\u00B9',
#         2: '\u00B2', 
#         3: '\u00B3', 
#         4: '\u2074', 
#         5: '\u2075', 
#         6: '\u2076', 
#         7: '\u2077', 
#         8: '\u2078', 
#         9: '\u2079'


from functions import write_file, read_file


def format_equation(text: str) -> list:
    if '\n' in text or '= 0' in text:
        text = text.replace('\n', '')
        text = text.replace('= 0', '')
    text = text.replace(' ', '')
    text = text.split('+')
    return text


def summation(first: list, second: list) -> str:
    result = ''
    if len(first) < len(second): 
        biggest = second
        small = first
    else: 
        biggest = first
        small = second

    biggest[-1] = str(int(small[-1]) + int(biggest[-1]))
    
    for elem in small:
        if 'x' in elem:
            power_numb = elem.split('x')
            for i in range(len(biggest)-1):
                power_numb_2 = biggest[i].split('x')
                if power_numb[1] == power_numb_2[1]:
                    biggest[i] = f'{int(power_numb[0])+int(power_numb_2[0])}x{power_numb[1]}'

    for elem in biggest:
        result += f'{elem} + '

    return result[:-3] + ' = 0'


first_equation = format_equation(read_file('004.txt'))
second_equation = format_equation(read_file('005.txt'))

print(first_equation)
print(second_equation)
print()

print(summation(first_equation, second_equation))
write_file('result.txt', summation(first_equation, second_equation))

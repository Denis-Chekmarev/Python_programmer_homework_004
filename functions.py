def get_number(text: str, error_text = 'Wrong input. Try again -> ') -> int:
    print(text, end='')
    while True:
        numb = input()
        if numb.isdigit():
            numb = float(numb)
            return numb
        else:
            print(error_text, end='')


def input_float_numb(text: str, error_text = 'Wrong input. Try again -> ') -> float:
    while True:
        number = input(text)
        try: 
            return float(number)
        except ValueError:
            print(error_text, end='')


code_power = {
        0: '\u2070',
        1: '\u00B9',
        2: '\u00B2', 
        3: '\u00B3', 
        4: '\u2074', 
        5: '\u2075', 
        6: '\u2076', 
        7: '\u2077', 
        8: '\u2078', 
        9: '\u2079'
    }
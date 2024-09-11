from typing import List


def fio(initials: List[str]) -> str:
    return ''.join([initials[0][0], initials[1][0], initials[2][0]])


def check_month(month: int):
    if month == 1 or month == 2 or month == 12:
        return 'Зима'
    elif month == 3 or month == 4 or month == 5:
        return 'Весна'
    elif month == 6 or month == 7 or month == 8:
        return 'Лето'
    elif month == 9 or month == 10 or month == 11:
        return 'Осень'
    else:
        return 'Некорректный номер месяца'


def square(square_side):
    perimeter = square_side * 4
    return perimeter

import unittest
from main import fio, check_month, square


class TestMain(unittest.TestCase):

    def test_fio_1(self):
        fio_list = ['Иванов', 'Иван', 'Иванович']
        expected = 'ИИИ'
        result = fio(fio_list)
        self.assertEqual(expected, result)

    def test_check_month_with_params(self):
        for i, (month, expected) in enumerate([
            (24, 'Некорректный номер месяца'),
            (1, 'Зима'),
            (4, 'Весна')
        ]):
            with self.subTest(i):
                result = check_month(month)
                self.assertEqual(expected, result)

    def test_square_with_params(self):
        for i, (square_side, expected) in enumerate([
            (10, 40),
            (9, 36)
        ]):
            with self.subTest(i):
                result = square(square_side)
                self.assertEqual(expected, result)

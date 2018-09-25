import unittest
from format_price import format_price


class TestPriceFormat(unittest.TestCase):

    def test_number_as_digits(self):
        self.assertEqual(format_price(3245.000000), '3 245')

    def test_number_as_string(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_number_not_whole(self):
        self.assertEqual(format_price('3245.67'), '3 245.67')

    def test_number_is_negative(self):
        self.assertEqual(format_price('-3245.67'), '-3 245.67')

    def test_zero(self):
        self.assertEqual(format_price(0), '0')

    def test_big_number(self):
        self.assertEqual(format_price('1234567890'), '1 234 567 890')

    def test_text(self):
        self.assertIsNone(format_price('test'))

    def test_bool(self):
        self.assertIsNone(format_price(True))

    def test_None(self):
        self.assertIsNone(format_price(None))

    def test_list(self):
        self.assertIsNone(format_price([3245]))

    def test_dict(self):
        self.assertIsNone(format_price({'price': 3245}))


if __name__ == '__main__':
    unittest.main()

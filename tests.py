import unittest
from format_price import format_price


class TestPriceFormat(unittest.TestCase):

    def test_number(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_text(self):
        self.assertRaises(ValueError, format_price, 'test')

    def test_list(self):
        self.assertRaises(TypeError, format_price, [3245])

    def test_dict(self):
        self.assertRaises(TypeError, format_price, {'price': 3245})

    def test_bool(self):
        self.assertRaises(TypeError, format_price, False)

    def test_None(self):
        self.assertRaises(TypeError, format_price, None)


if __name__ == '__main__':
    unittest.main()

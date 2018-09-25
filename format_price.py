import sys


def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price = round(float(price), 2)
    except (TypeError, ValueError):
        return None
    return '{0:,.{1}f}'.format(
        price, '0' if price.is_integer() else '2'
        ).replace(',', ' ')


if __name__ == '__main__':
    try:
        print(format_price(sys.argv[1]))
    except IndexError:
        print('Enter number to format')

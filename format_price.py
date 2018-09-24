import sys


def format_price(price):
    if not price or isinstance(price, bool):
        raise TypeError('Argument must be a string or a number')
    else:
        return '{:,.0f}'.format(float(price)).replace(',', ' ')


if __name__ == '__main__':
    try:
        print(format_price(sys.argv[1]))
    except IndexError:
        print('Enter number to format')
    except (TypeError, ValueError) as err:
        print(err)

# Price Formatter

Script that outputs a number in more human-readable form, e.g. `3245.000000` becomes `3 245`. You can run it from console or import as module.

## Quick Start

To run it from console:
```bash
$ python format_price.py 3245.000000
3 245
```
Use in your own script:
```python
from format_price import format_price
print(format_price('3245.000000'))  # -> 3 245
```

## Testing

```bash
$ python tests.py
...........
----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK
```


## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

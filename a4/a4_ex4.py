def round_(number, ndigits: int = None):
    rounded_float = 0.0
    if ndigits is not None: 
        factor = 10 ** ndigits
        rounded_integer = int(number * factor + .5)
        rounded_float = rounded_integer / factor
    return int(number + .5) if ndigits is None else rounded_float


# print(round_(777.777))
# print(round_(777.777, 0))
# print(round_(777.777, 1))
# print(round_(777.777, 2))
# print(round_(777.777, 3))
# print(round_(777.777, 4))
def gen_fibonacci(upper_bound):
    try:
        if not isinstance(upper_bound, (int, float)):
            raise TypeError
        elif upper_bound < 0:
            raise ValueError
        
        a, b = 0, 1
        while a <= upper_bound:
            yield a
            a, b = b, a + b
    except TypeError:
        print("upper_bound must be an integer or a float")
    except ValueError:
        print("upper_bound must be non-negative")
        
# res = list(gen_fibonacci("3"))
# print(res)
# res = list(gen_fibonacci(-1))
# print(res)
# res = list(gen_fibonacci(0))
# print(res)
# res = list(gen_fibonacci(1))
# print(res)
# res = list(gen_fibonacci(3))
# print(res)
# res = list(gen_fibonacci(9.2))
# print(res)
class Power:
    def __init__(self, exponent):
        if isinstance(exponent, (int, float)):
            self.exponent = exponent
        else:
            raise TypeError("The exponent must be a numerical value.")
    
    def __call__(self, x):
        if isinstance(x, (int, float)):
            return x ** self.exponent
        else:
            raise TypeError("Input must be a numerical value.")
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # self.exponent += other
            return Power(self.exponent + other)
        elif isinstance(other, Power):
            return Power(self.exponent + other.exponent)
        else:
            raise NotImplemented
        
class Square(Power):
    def __init__(self):
        super().__init__(2)
        
if __name__ == '__main__':
    x = 3
    square = Square()
    cube = Power(3)
    print(square.exponent, square(x))
    print(cube.exponent, cube(x))
    
    m1 = square * 2
    print(m1.exponent, m1.__call__(x))
    m2 = square * cube
    print(m2.exponent, m2.__call__(x))
    
    try :
        square("foo")
    except TypeError as e:
        print(e)
    try :
        Power("foo")
    except TypeError as e:
        print(e)
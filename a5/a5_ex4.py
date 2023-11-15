def f(x: int):
    try:
        g(x)
        print("f1")
    except ErrorA:
        print("f2")
    finally:
        print("f3")

def g(x: int):
    try:
        h(x)
        print("g1")
    except ErrorA:
        print("g2")
    except ErrorB:
        print("g3")
        if x < -10:
            raise ErrorC
            print("g4")
        else:
            print("g5")
            print("g6")

def h(x: int):
    try:
        if x > 10:
            raise ErrorA
        if x < 0:
            raise ErrorB
    finally:
        print("h1")
    print("h2")
        
        
class ErrorA(Exception):
    def __init__(self):
        super().__init__("ErrorA")
    
class ErrorB(Exception):
    def __init__(self):
        super().__init__("ErrorB")
        
class ErrorC(Exception):
    def __init__(self):
        super().__init__("ErrorC")  

        
        
f(-11)
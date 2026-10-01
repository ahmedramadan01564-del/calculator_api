def add(a: float, b:float) -> float:
    """Adds two number and return result"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Differenc between two number and return result"""
    return a - b

def multibly(a: float, b:float) -> float:
    """product two number and return result"""
    return a * b

def divide(a: float, b: float) -> float:
    """return quotient two number  and return result"""
    return a / b

OPERATIONS = {
    "+" : add,
    "-" : subtract,
    "*" : multibly,
    "/" : divide,
}
class  Complex:
    a: float
    b: float

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __add__(self, other: Complex) -> Complex:
        return Complex(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other: Complex) -> Complex:
        return Complex(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other: Complex) -> Complex:
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
    
    def __truediv__(self, other: Complex) -> Complex:
        d = other.a**2 + other.b**2

        return Complex((self.a * other.a + self.b * other.b)/d, (self.b * other.a - self.a * other.b)/d)
    
    def __repr__(self):
        if self.b < 0:
            b = -self.b

            if b == 1:
                return f'({self.a} - i)'

            return f'({self.a} - {b}i)'    
        
        if self.b == 1:
            return f'({self.a} + i)'

        return f'({self.a} + {self.b}i)'

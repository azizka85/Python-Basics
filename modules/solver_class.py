from typing import Tuple
from math import sqrt, pi, atan

class Solver:
    g: float

    H: float
    L: float

    def __init__(self, g: float, H: float, L: float):
        self.g = g

        self.H = H
        self.L = L

    def calc_v0_min(self) -> float:
        S = sqrt(self.H**2 + self.L**2)

        v0 = sqrt(self.g*(self.H + S))

        return v0
    
    def calc_D(self, v: float) -> float:
        D = v**4/self.g**2/self.L**2 - 2*v**2*self.H/self.g/self.L**2 - 1

        return D
    
    def calc_p(
        self,
        v: float, D: float        
    ) -> Tuple[float, float]:
        p1 = v**2/self.g/self.L - sqrt(D)
        p2 = v**2/self.g/self.L + sqrt(D)

        return p1, p2
    
    @classmethod
    def calc_angle(cls, p: float) -> float:
        theta = atan(p)*180/pi    

        return theta
    
    def calc_flight_time(self, v: float, p: float) -> float:
        T = self.L*sqrt(1 + p**2)/v

        return T

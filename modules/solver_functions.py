from typing import Tuple
from math import sqrt, pi, atan

def calc_v0_min(g: float, H: float, L: float) -> float:
    S = sqrt(H**2 + L**2)

    v0 = sqrt(g*(H + S))

    return v0

def calc_D(
    v: float, 
    g: float, H: float, L: float
) -> float:
    D = v**4/g**2/L**2 - 2*v**2*H/g/L**2 - 1

    return D

def calc_p(
    v: float, D: float, 
    g: float, L: float
) -> Tuple[float, float]:
    p1 = v**2/g/L - sqrt(D)
    p2 = v**2/g/L + sqrt(D)

    return p1, p2

def calc_angle(
    p: float
) -> float:
    theta = atan(p)*180/pi    

    return theta

def calc_flight_time(v: float, p: float, L: float) -> float:
    T = L*sqrt(1 + p**2)/v

    return T

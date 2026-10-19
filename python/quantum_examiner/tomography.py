from dataclasses import dataclass

@dataclass(frozen=True)
class TomographyResult:
    x: float
    y: float
    z: float
    purity: float
    physical: bool

def estimate_single_qubit(x_plus, x_minus, y_plus, y_minus, z_plus, z_minus):
    def diff(a,b):
        total = a+b
        if total <= 0:
            raise ValueError('Each basis requires at least one sample')
        return (a-b)/total
    x, y, z = diff(x_plus,x_minus), diff(y_plus,y_minus), diff(z_plus,z_minus)
    r2 = x*x+y*y+z*z
    return TomographyResult(x,y,z,(1+r2)/2,r2 <= 1+1e-9)

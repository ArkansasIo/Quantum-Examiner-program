from __future__ import annotations
from dataclasses import dataclass
import cmath
import math

@dataclass(frozen=True)
class BlochVector:
    x: float
    y: float
    z: float

    def norm(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def is_physical(self, tolerance: float = 1e-9) -> bool:
        return self.norm() <= 1.0 + tolerance

@dataclass
class QubitState:
    alpha: complex = 1 + 0j
    beta: complex = 0 + 0j

    def normalize(self) -> None:
        n = math.sqrt(abs(self.alpha)**2 + abs(self.beta)**2)
        if n == 0:
            raise ValueError('State vector cannot be zero')
        self.alpha /= n
        self.beta /= n

    def probabilities(self):
        self.normalize()
        return abs(self.alpha)**2, abs(self.beta)**2

    def bloch(self) -> BlochVector:
        self.normalize()
        c = self.alpha.conjugate() * self.beta
        return BlochVector(2*c.real, 2*c.imag,
                           abs(self.alpha)**2 - abs(self.beta)**2)

    @classmethod
    def from_bloch(cls, v: BlochVector) -> 'QubitState':
        if not v.is_physical():
            raise ValueError('Bloch vector lies outside the physical unit ball')
        r = v.norm()
        if r < 1e-12:
            return cls(1/math.sqrt(2), 1/math.sqrt(2))
        theta = math.acos(max(-1.0, min(1.0, v.z/r)))
        phi = math.atan2(v.y, v.x)
        return cls(math.cos(theta/2), cmath.exp(1j*phi)*math.sin(theta/2))

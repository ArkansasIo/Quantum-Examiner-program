# Wolfmoon Alpha Mathematics
# Isolated mathematical primitives for the examiner.
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Vector3:
    x: float
    y: float
    z: float
    def norm(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def normalized(self):
        n=self.norm()
        if n == 0: raise ValueError('Cannot normalize zero vector')
        return Vector3(self.x/n,self.y/n,self.z/n)

def spherical_to_cartesian(theta, phi):
    return Vector3(math.sin(theta)*math.cos(phi), math.sin(theta)*math.sin(phi), math.cos(theta))

def cartesian_to_spherical(v):
    n=v.norm()
    if n == 0: raise ValueError('Zero vector has no spherical coordinates')
    return math.acos(max(-1,min(1,v.z/n))), math.atan2(v.y,v.x)

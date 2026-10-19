from dataclasses import dataclass, asdict
import json
from .state import BlochVector

@dataclass
class Examination:
    physical: bool
    radius: float
    warnings: list[str]
    provenance: dict
    def to_json(self):
        return json.dumps(asdict(self), indent=2)

def examine_bloch(v: BlochVector, provenance=None):
    radius = v.norm()
    warnings=[]
    if radius > 1.000001:
        warnings.append('Bloch vector is outside the physical unit ball.')
        warnings.append('Check calibration, noise correction, and measurement normalization.')
    return Examination(radius <= 1.000001, radius, warnings, provenance or {})

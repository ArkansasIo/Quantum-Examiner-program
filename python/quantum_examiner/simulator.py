from __future__ import annotations
import numpy as np

class StateVectorSimulator:
    def __init__(self, qubits: int = 1):
        if qubits < 1:
            raise ValueError('qubits must be >= 1')
        self.qubits = qubits
        self.state = np.zeros(2**qubits, dtype=complex)
        self.state[0] = 1.0

    def apply_single(self, gate: np.ndarray, target: int) -> None:
        if gate.shape != (2,2):
            raise ValueError('gate must be 2x2')
        if not 0 <= target < self.qubits:
            raise IndexError('target out of range')
        full = np.array([[1]], dtype=complex)
        for q in range(self.qubits):
            full = np.kron(full, gate if q == target else np.eye(2))
        self.state = full @ self.state

    def probabilities(self):
        return np.abs(self.state)**2

    def measure(self, shots=1024, rng=None):
        rng = rng or np.random.default_rng()
        samples = rng.choice(len(self.state), size=shots, p=self.probabilities())
        counts = {}
        for s in samples:
            key = format(int(s), f'0{self.qubits}b')
            counts[key] = counts.get(key, 0) + 1
        return counts

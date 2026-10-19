from quantum_examiner.state import QubitState
from quantum_examiner.tomography import estimate_single_qubit

def test_zero_state():
    b=QubitState().bloch()
    assert b.x==0 and b.y==0 and b.z==1

def test_plus_x():
    q=QubitState(1,1); q.normalize(); b=q.bloch()
    assert abs(b.x-1)<1e-9 and abs(b.y)<1e-9 and abs(b.z)<1e-9

def test_tomography():
    r=estimate_single_qubit(100,0,50,50,50,50)
    assert r.physical and abs(r.x-1)<1e-9

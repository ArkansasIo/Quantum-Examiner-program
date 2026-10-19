import numpy as np

X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)
H = np.array([[1,1],[1,-1]], dtype=complex) / np.sqrt(2)
S = np.array([[1,0],[0,1j]], dtype=complex)
T = np.array([[1,0],[0,np.exp(1j*np.pi/4)]], dtype=complex)

def rx(theta):
    return np.array([[np.cos(theta/2),-1j*np.sin(theta/2)],
                     [-1j*np.sin(theta/2),np.cos(theta/2)]], dtype=complex)

def ry(theta):
    return np.array([[np.cos(theta/2),-np.sin(theta/2)],
                     [np.sin(theta/2),np.cos(theta/2)]], dtype=complex)

def rz(theta):
    return np.array([[np.exp(-1j*theta/2),0],
                     [0,np.exp(1j*theta/2)]], dtype=complex)

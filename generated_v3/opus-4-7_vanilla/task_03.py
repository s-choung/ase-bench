from ase import Atoms
import numpy as np

a = 3.16
c_MoS = 1.59
vacuum = 10.0

cell = [[a, 0, 0],
        [-a/2, a*np.sqrt(3)/2, 0],
        [0, 0, 2*c_MoS + vacuum]]

z_mid = (2*c_MoS + vacuum) / 2
positions = [
    [0, 0, z_mid],
    [a/2, a*np.sqrt(3)/6, z_mid - c_MoS],
    [a/2, a*np.sqrt(3)/6, z_mid + c_MoS],
]

mos2 = Atoms('MoS2', positions=positions, cell=cell, pbc=[True, True, True])

print("Cell:")
print(mos2.cell[:])
print("Cell lengths:", mos2.cell.lengths())
print("Cell angles:", mos2.cell.angles())

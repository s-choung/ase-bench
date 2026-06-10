from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms('CO2', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]], cell=(10, 10, 10), pbc=False)
D, D_len = get_distances([0, 1, 2], [0, 1, 2], cell=atoms.cell, pbc=atoms.pbc)
print(D_len[1:, 0])

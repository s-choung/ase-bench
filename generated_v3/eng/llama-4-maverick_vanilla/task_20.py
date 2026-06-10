from ase.build import nanotube
from ase import Atoms

cnt = nanotube(6, 6, length=4)
print(f"Number of atoms: {len(cnt)}")
print("Cell info:")
print(cnt.cell)

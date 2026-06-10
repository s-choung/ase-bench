from ase.build import nanotube
from ase import Atoms

cnt = nanotube(6, 6, length=4)

print(f"Number of atoms: {len(cnt)}")
print(f"Cell:\n{cnt.cell}")
print(f"Cell lengths and angles: {cnt.cell.cellpar()}")
print(f"Chemical formula: {cnt.get_chemical_formula()}")

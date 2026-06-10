from ase.build import nanotube
from ase import Atoms

atoms = nanotube(6, 6, length=4)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell lengths and angles: {atoms.get_cell_lengths_and_angles()}")

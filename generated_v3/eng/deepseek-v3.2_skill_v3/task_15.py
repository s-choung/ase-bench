from ase.build import fcc100
from ase.visualize import view

atoms = fcc100('Cu', size=(3,3,3), vacuum=12.0)
print(f"Number of atoms: {len(atoms)}")
print(f"Cell vectors:\n{atoms.get_cell()}")
print(f"Cell lengths and angles: {atoms.get_cell_lengths_and_angles()}")

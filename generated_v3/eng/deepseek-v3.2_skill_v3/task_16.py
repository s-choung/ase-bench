from ase.build import bcc110
from ase.visualize import view

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell size: {atoms.cell.lengths()}")

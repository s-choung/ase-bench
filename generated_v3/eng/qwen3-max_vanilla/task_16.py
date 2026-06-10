from ase.build import bcc110
from ase import Atoms

# Create Fe BCC(110) surface with 4 layers, 2x2 surface unit cell, and 10 Å vacuum
atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Print number of atoms and cell size
print(f'Number of atoms: {len(atoms)}')
print(f'Cell size (Å): {atoms.cell.cellpar()[:3]}')

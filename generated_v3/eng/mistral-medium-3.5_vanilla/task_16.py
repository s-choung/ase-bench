from ase.lattice.surface import bcc110
from ase.build import add_vacuum

atoms = bcc110('Fe', size=(2, 2, 4))
add_vacuum(atoms, 10)
print(f"Number of atoms: {len(atoms)}")
print(f"Cell size: {atoms.cell.lengths()}")

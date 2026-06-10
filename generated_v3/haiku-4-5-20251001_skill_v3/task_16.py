from ase.build import bcc110, add_vacuum
from ase import units

atoms = bcc110('Fe', size=(2,2,4), a=2.87, vacuum=10.0)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell: {atoms.get_cell()}")
print(f"Cell lengths and angles: {atoms.get_cell_lengths_and_angles()}")

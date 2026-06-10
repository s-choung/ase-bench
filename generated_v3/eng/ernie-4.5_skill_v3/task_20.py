from ase import Atoms
from ase.build import nanotube

# Create (6,6) carbon nanotube with length=4
atoms = nanotube(6, 6, length=4, bond=1.42, symbol='C')

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print cell information
cell = atoms.get_cell()
lengths, angles = atoms.get_cell_lengths_and_angles()
print(f"Cell lengths (Å): {lengths}")
print(f"Cell angles (degrees): {angles}")

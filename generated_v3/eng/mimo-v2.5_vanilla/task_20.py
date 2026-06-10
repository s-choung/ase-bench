from ase.build import nanotube
from ase import Atoms

# Create (6,6) carbon nanotube with length=4 unit cells
nanotube_atoms = nanotube(n=6, m=6, length=4, bond=1.42)

# Print number of atoms
print(f"Number of atoms: {len(nanotube_atoms)}")

# Print cell info (dimensions and angles)
cell = nanotube_atoms.cell
print(f"Cell vectors (Å):")
print(f"  a = {cell[0]}")
print(f"  b = {cell[1]}")
print(f"  c = {cell[2]}")
print(f"Cell angles: {cell.angles()}")

from ase.build import nanotube
from ase import units

# Create a (6,6) carbon nanotube with a length of 4 Angstroms
c_nanotube = nanotube(n=6, m=6, length=4, bond=1.42)

# Print the number of atoms
print(f"Number of atoms: {len(c_nanotube)}")

# Print the cell information
cell = c_nanotube.get_cell()
print(f"Cell lengths: {cell.lengths()}")
print(f"Cell angles: {cell.angles()}")

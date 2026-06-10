from ase.build import fcc100
from ase.build import bulk

# Alternatively, using bulk to then create the surface if needed, but fcc100 is direct.
# Here, using fcc100 which directly provides a fcc(100) surface

# Build a Cu(100) surface with 3 layers
atoms = fcc100('Cu', size=(3, 3, 3), layers=3, vacuum=12.0)

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print cell information
print(f"Cell info (lattice vectors in Å): {atoms.cell}")

# If you want to visualize in a non-GUI text form the cell vectors and diagonal:
print(f"Cell lengths: {atoms.cell.cell_lengths()}")
print(f"Cell angles: {atoms.cell.cell_angles()}")

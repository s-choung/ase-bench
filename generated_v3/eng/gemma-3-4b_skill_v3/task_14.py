from ase import Atoms
from ase.spacegroup import crystal

# Define spacegroup 225 (Fm-3m)
spacegroup = crystal('Na', 'Cl', spacegroup=225, size=(2, 2, 2))

# Define lattice constant
a = 5.64

# Create the crystal structure
atoms = Atoms(positions=spacegroup.positions, cell=spacegroup.cell, latticeconstant=a)

# Print the number of atoms
print(len(atoms))

# Print the chemical symbols
print(atoms.symbols)

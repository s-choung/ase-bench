from ase import Atoms
from ase.build import bulk

# Create a Cu FCC bulk
a = 3.6  # lattice constant of Cu in Angstrom
Cu_bulk = bulk("Cu", "fcc", a=a)

# Create a 2x2x2 supercell
supercell = Cu_bulk*(2,2,2)

print(supercell.cell)  # Print cell info
print("Number of atoms:", len(supercell))  # Print number of atoms

from ase.build import bulk
from ase import Atoms

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Generate 2x2x2 supercell
cu_supercell = cu_bulk * (2, 2, 2)

# Print cell info and number of atoms
print("Cell:")
print(cu_supercell.cell)
print("Number of atoms:", len(cu_supercell))

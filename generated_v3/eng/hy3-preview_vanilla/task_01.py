from ase.build import bulk
from ase.io import write

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Generate 2x2x2 supercell
supercell = cu_bulk.repeat((2, 2, 2))

# Print cell info and number of atoms
print("Original cell:\n", cu_bulk.cell)
print("\nSupercell:\n", supercell.cell)
print("\nNumber of atoms in supercell:", len(supercell))

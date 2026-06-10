from ase.build import bulk
from ase.visualize import view

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.61)

# Generate 2x2x2 supercell
supercell = cu_bulk.repeat((2, 2, 2))

# Print cell info and number of atoms
print("Cell info:", supercell.get_cell())
print("Number of atoms:", len(supercell))

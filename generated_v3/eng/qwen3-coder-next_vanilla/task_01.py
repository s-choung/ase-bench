from ase import Atoms
from ase.build import bulk

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.61)

# Generate 2x2x2 supercell
cu_supercell = cu_bulk * (2, 2, 2)

# Print cell info and number of atoms
print("Supercell cell vectors:")
print(cu_supercell.cell)
print(f"Number of atoms: {len(cu_supercell)}")

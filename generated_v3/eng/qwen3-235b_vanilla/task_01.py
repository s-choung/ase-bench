from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Generate 2x2x2 supercell
supercell = cu_bulk * (2, 2, 2)

# Print cell info and number of atoms
print("Cell vectors:\n", supercell.get_cell())
print("Number of atoms:", len(supercell))

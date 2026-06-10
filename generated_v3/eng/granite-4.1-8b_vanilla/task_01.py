from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk

# Create Cu FCC bulk structure
cu_bulk = bulk('Cu', 'fcc', a=3.615)

# Generate a 2x2x2 supercell
supercell = cu_bulk.repeat((2, 2, 2))

# Assign a simple calculator (EMT) for demonstration purposes
supercell.set_calculator(EMT())

# Print cell information and number of atoms
print(supercell.cell)
print(f"Number of atoms: {supercell.get_number_of_atoms()}")

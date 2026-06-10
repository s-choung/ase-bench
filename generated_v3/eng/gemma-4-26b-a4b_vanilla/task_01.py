from ase.build import bulk
from ase.calculators.emt import EMT

# Create Cu FCC bulk (using EMT for demonstration as it is a built-in calculator)
# Note: EMT is for metals, though Cu parameters aren't physically accurate for EMT
atoms = bulk('Cu', 'fcc', a=3.6)

# Generate a 2x2x2 supercell
supercell = atoms * (2, 2, 2)

# Attach calculator
supercell.calc = EMT()

# Print cell info and number of atoms
print(f"Cell vectors:\n{supercell.cell}")
print(f"Number of atoms: {len(supercell)}")

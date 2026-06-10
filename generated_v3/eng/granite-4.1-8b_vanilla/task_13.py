from ase import Atoms
from ase.calculators.emt import EMT
from ase.lattice.cubic import Diamond

# Create Si bulk with diamond structure and lattice constant 5.43 Å
si = Diamond("Si", latticeconstant=5.43)

# Create a 3x3x3 supercell
supercell = si.repeat(3)

# Assign a simple calculator (EMT) for demonstration; not used for properties
supercell.calc = EMT()

# Print the number of atoms and the cell volume
print("Number of atoms:", supercell.natoms)
print("Cell volume (Å³):", supercell.cell.volume * 1.0)  # Cell volume is in Å³ by default

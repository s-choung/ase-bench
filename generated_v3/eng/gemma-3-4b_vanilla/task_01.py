from ase.build import fcc111
from ase.calculators import EMT
from ase.geometry import point_symmetry
from ase.io import write

# Create a Cu FCC bulk
cell = fcc111('Cu', size=(3, 3, 3), direction=(1, 1, 1))

# Generate a 2x2x2 supercell
supercell = cell.copy()
supercell.translate((0, 0, 0))
supercell.translate((1, 1, 1))
supercell.translate((2, 2, 2))

# Set the calculator to EMT
calculator = EMT()
supercell.calc = calculator

# Calculate the electronic properties
supercell.get_atomic_properties()

# Print the cell info
print("Cell:", supercell.cell)

# Print the number of atoms
print("Number of atoms:", len(supercell))

# Write the supercell to a file
write('Cu_supercell.traj', supercell)

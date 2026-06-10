from ase.build import surface
from ase.build import bulk
from ase.geometry import cell_to_cellpar

# Create BCC iron structure and the (110) surface
atoms = bulk('Fe', 'bcc', a=2.87, cubic=True)
surface_structure = surface(atoms, (1, 1, 0), layers=4, vacuum=10)

# Adjust size to (2, 2, 4)
surface_structure = surface_structure.repeat((2, 2, 4))

# Print the number of atoms
print(f"Number of atoms: {len(surface_structure)}")

# Print the cell size
cell_parameters = cell_to_cellpar(surface_structure.cell)
print(f"Cell parameters (a, b, c, alpha, beta, gamma): {cell_parameters}")

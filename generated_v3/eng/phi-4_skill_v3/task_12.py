from ase.build import bulk
from ase.geometry import find_molecule
from ase.thermochemistry import IdealGasThermo
from ase.units import angstrom

# Define lattice parameters for Ti hcp
a, c = 2.95, 1.59 * 2.95

# Create bulk structure
atoms = bulk('Ti', structure='hexagonal', a=a, c=c)

# Print lattice vectors
print("Lattice Vectors (in angstrom):")
print(atoms.get_cell().get_cell_lengths_and_angles())

# Print atomic positions
print("Atomic Positions (in Bohr):")
positions = atoms.get_positions()
print(positions)

# Optionally, visualize the structure
# from ase.visualize import view
# view(atoms)

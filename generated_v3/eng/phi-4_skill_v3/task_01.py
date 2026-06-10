from ase import Atoms
from ase.build import bulk
from ase.visualize import view

# Create a Cu bulk with an FCC structure
atoms = bulk('Cu', crystal_structure='fcc', a=3.65, cubic=True)

# Create a supercell by repeating the unit cell
supercell = atoms.repeat((2, 2, 2))

# Print cell information
print("Supercell unit cell:", supercell.get_cell())

# Print the number of atoms in the supercell
print("Number of atoms:", supercell.get_number_of_atoms())

# Optionally, visualize the supercell (requires an external viewer)
# view(supercell)

# Example information output (note that view command uses external tools)
# Supercell unit cell: [[6.0, 0.0, 0.0], [0.0, 6.0, 0.0], [0.0, 0.0, 6.0]]
# Number of atoms: 16

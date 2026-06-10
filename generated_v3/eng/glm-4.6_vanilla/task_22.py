from ase.build import fcc111, molecule
from ase import Atoms

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Create N2 molecule
n2 = molecule('N2')
n2.center()

# Position N2 on bridge site at 2.0 Å height
bridge_pos = slab[0].position + slab[1].position
bridge_pos = bridge_pos / 2
bridge_pos[2] = slab[0].position[2] + 2.0
n2.translate(bridge_pos - n2.get_center_of_mass())

# Combine slab and N2
structure = slab + n2

# Print information
print(f"Number of atoms: {len(structure)}")
print("Atom types:", sorted(set(structure.get_chemical_symbols())))

from ase.build import bulk, add_adsorbate
from ase import Atoms

# Create bulk MoS2
atoms = bulk('MoS2', 'hexagonal', a=3.16, c=12.3)

# Isolate a single layer (remove periodic images in c)
atoms = atoms[atoms.get_chemical_symbols() == 'Mo'] | atoms[atoms.get_chemical_symbols() == 'S']
# Center in the layer
atoms.center(vacuum=10, axis=2)

# Ensure vacuum thickness is 10 Angstrom above and below
print(f'Cell size: {atoms.get_cell().diagonal()}')

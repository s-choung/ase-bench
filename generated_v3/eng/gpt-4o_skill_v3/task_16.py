from ase.build import bcc110
from ase import units

surface = bcc110('Fe', size=(2, 2, 4), vacuum=10)
print(f'Number of atoms: {len(surface)}')
print(f'Cell size: {surface.get_cell_lengths_and_angles()}')

from ase.build import mx2
from ase import units

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10)
cell = atoms.get_cell_lengths_and_angles()
print('Cell size (a, b, c):', cell[:3])

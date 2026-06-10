from ase.build import mx2
from ase import units

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)
atoms = atoms + 10 * units.Angstrom
cell_lengths_and_angles = atoms.get_cell_lengths_and_angles()

print(cell_lengths_and_angles)

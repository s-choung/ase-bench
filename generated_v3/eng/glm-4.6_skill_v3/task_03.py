from ase.build import mx2, add_vacuum
from ase.units import Bohr

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)
add_vacuum(atoms, 10.0)
cell = atoms.get_cell()
print(f"Cell vectors (Angstrom):\n{cell}")
print(f"Cell lengths and angles: {atoms.get_cell_lengths_and_angles()}")

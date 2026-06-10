from ase import Atoms
from ase.build import nanotube

tube = nanotube(6, 6, length=4, bond=1.42, symbol='C')
print(f"Number of atoms: {len(tube)}")
print(f"Cell:\n{tube.get_cell()}")
print(f"Cell lengths and angles: {tube.get_cell_lengths_and_angles()}")

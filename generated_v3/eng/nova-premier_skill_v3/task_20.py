from ase import Atoms
from ase.build import nanotube

tube = nanotube(6, 6, length=4, bond=1.42, vacuum=5)
tube.info = {"type": "CNT_6_6"}
print(f"N_atoms={len(tube)}")
print(tube.get_cell_lengths_and_angles())

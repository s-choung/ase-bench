from ase.build import nanotube
from ase import units

cnt = nanotube(6, 6, length=4, vacuum=5.0)
print(f"Number of atoms: {len(cnt)}")
print("Cell lengths (Å):", cnt.get_cell_lengths_and_angles()[:3])
print("Cell angles (°):", cnt.get_cell_lengths_and_angles()[3:])

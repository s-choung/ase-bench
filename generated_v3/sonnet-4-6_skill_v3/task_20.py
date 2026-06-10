from ase.build import nanotube
from ase import units

cnt = nanotube(6, 6, length=4, bond=1.42, symbol='C')

print(f"Number of atoms: {len(cnt)}")
print(f"Cell:\n{cnt.get_cell()}")
print(f"Cell lengths and angles: {cnt.get_cell_lengths_and_angles()}")
print(f"PBC: {cnt.get_pbc()}")

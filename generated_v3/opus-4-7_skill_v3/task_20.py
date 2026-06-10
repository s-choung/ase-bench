from ase.build import nanotube

cnt = nanotube(6, 6, length=4)
print(f"Atoms: {len(cnt)}")
print(f"Cell:\n{cnt.get_cell()}")
print(f"Cell lengths and angles: {cnt.cell.cellpar()}")
print(f"PBC: {cnt.pbc}")

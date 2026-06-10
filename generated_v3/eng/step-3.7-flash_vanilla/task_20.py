from ase.build import nanotube

cnt = nanotube(6, 6, length=4)
print(f"Number of atoms: {len(cnt)}")
print("Cell (Å):\n", cnt.cell)

from ase.build import nanotube

n = nanotube((6, 6), length=4, periodic=True)
print(f"Number of atoms: {len(n)}")
print(f"Cell:\n{n.get_cell()}")

from ase.build import fcc100

surf = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
print(f"Number of atoms: {len(surf)}")
print(f"Cell: {surf.cell}")

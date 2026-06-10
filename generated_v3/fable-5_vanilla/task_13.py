from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
supercell = si * (3, 3, 3)

print("Number of atoms:", len(supercell))
print("Cell volume (A^3):", supercell.get_volume())

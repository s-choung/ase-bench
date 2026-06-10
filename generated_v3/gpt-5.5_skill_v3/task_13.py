from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43, cubic=True)
si_super = si * (3, 3, 3)

print("Number of atoms:", len(si_super))
print("Cell volume (Ang^3):", si_super.get_volume())

from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
si = si.repeat((3, 3, 3))
print("Number of atoms:", len(si))
print("Cell volume:", si.get_volume())

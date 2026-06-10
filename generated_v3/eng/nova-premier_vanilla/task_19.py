from ase import Atoms

co2 = Atoms('COO', [(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)], cell=[10, 10, 10], pbc=False)
dists = co2.get_distances(0, [1, 2])
print("C-O distances:", dists)

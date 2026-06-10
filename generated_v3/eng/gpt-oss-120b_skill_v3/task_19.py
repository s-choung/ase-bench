from ase import Atoms

# C at origin, O atoms ±1.16 Å along z
positions = [(0, 0, 0), (0, 0, 1.16), (0, 0, -1.16)]
atoms = Atoms('CO2', positions=positions, cell=[10, 10, 10], pbc=False)

# interatomic distance matrix (Å)
dist_matrix = atoms.get_all_distances()
print(dist_matrix)

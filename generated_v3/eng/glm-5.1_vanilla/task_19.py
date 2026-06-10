from ase import Atoms

atoms = Atoms('CO2', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]], cell=[10, 10, 10], pbc=False)

print("C-O distances:", atoms.get_distances(0, [1, 2]))
print("O-O distance:", atoms.get_distances(1, 2))

from ase import Atoms

atoms = Atoms('COO', positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)])
atoms.set_cell([10, 10, 10])
atoms.set_pbc(False)

print(atoms.get_distances(0, 1))
print(atoms.get_distances(0, 2))
print(atoms.get_distances(1, 2))

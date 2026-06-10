from ase import Atoms

atoms = Atoms('COO', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]],
              cell=[10, 10, 10], pbc=False)

i = [0, 0, 1]
j = [1, 2, 2]
print(atoms.get_distances(i, j))

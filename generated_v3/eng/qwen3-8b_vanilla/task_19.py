from ase import Atoms

atoms = Atoms(symbols=['C', 'O', 'O'],
              positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]],
              cell=[10, 10, 10],
              pbc=False)
print(atoms.get_distances())

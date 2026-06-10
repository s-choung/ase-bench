from ase import Atoms

atoms = Atoms(symbols=['C', 'O', 'O'],
              positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)],
              cell=[10, 10, 10], pbc=False)

distances = atoms.get_distances(atoms.get_positions())
print("Interatomic distances (Å):")
print(distances)

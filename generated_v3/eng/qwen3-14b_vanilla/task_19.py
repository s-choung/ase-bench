from ase import Atoms

atoms = Atoms('CO2',
              positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]],
              cell=[10, 10, 10],
              pbc=False)

print(f"C-O1: {atoms.get_distances(0, 1):.3f} Å")
print(f"C-O2: {atoms.get_distances(0, 2):.3f} Å")
print(f"O1-O2: {atoms.get_distances(1, 2):.3f} Å")

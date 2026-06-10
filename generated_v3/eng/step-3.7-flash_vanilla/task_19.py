from ase import Atoms
mol = Atoms('CO2', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]], cell=[10, 10, 10], pbc=False)
print(mol.get_distances(i=[0, 0, 1], j=[1, 2, 2]))

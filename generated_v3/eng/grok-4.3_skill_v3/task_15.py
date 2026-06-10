from ase.build import fcc100
atoms = fcc100('Cu', size=(3,3,3), vacuum=12)
print(len(atoms), atoms.get_cell())

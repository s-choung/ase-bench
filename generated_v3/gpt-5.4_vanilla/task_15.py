from ase.build import fcc100

atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

print(len(atoms))
print(atoms.cell)

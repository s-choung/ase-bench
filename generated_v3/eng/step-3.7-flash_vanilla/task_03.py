from ase.build import mos2
atoms = mos2(vacuum=10)
print(atoms.cell)

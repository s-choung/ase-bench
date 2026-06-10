from ase import Atoms
atoms = Atoms('Al', 'bcc', a=3.3, cubic=True)
print(atoms.cell)
print(atoms.get_chemical_symbols())

from ase import Atoms

a = 5.64
cell = [[a, 0, 0], [0, a, 0], [0, 0, a]]
positions = [[0.0, 0.0, 0.0], [0.5, 0.5, 0.5]]
atoms = Atoms('NaCl', positions=positions, cell=cell, pbc=True)

print(len(atoms))
print(atoms.get_chemical_symbols())

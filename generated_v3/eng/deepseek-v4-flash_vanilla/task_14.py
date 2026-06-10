from ase.build import bulk

atoms = bulk('NaCl', 'rocksalt', a=5.64)
print(len(atoms), atoms.get_chemical_symbols())

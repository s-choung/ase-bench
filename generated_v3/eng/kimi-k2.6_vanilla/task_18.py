from ase.build import molecule

atoms = molecule('CH4')
print(atoms.get_chemical_formula())
print(atoms.positions)

c = [i for i, s in enumerate(atoms.symbols) if s == 'C'][0]
for h in [i for i, s in enumerate(atoms.symbols) if s == 'H']:
    print(atoms.get_distance(c, h))

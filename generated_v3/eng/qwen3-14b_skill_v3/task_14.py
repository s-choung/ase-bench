from ase.spacegroup import crystal

atoms = crystal(symbols=['Na', 'Cl'], positions=[(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, a=5.64)
print(len(atoms))
print(atoms.get_chemical_symbols())

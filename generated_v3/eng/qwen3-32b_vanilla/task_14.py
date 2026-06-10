from ase.spacegroup import Spacegroup

a = 5.64
sg = Spacegroup(225)
atoms = sg.make_crystal(['Na', 'Cl'], [[0, 0, 0], [0.5, 0.5, 0.5]], latticeconstants=(a, a, a, 90, 90, 90))
print(len(atoms))
print(atoms.get_chemical_symbols())

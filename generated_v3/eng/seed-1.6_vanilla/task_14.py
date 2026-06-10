from ase.spacegroup import crystal
from ase.calculators.emt import EMT

cellpar = [5.64, 5.64, 5.64, 90, 90, 90]
atoms = crystal(['Na', 'Cl'], basis=[(0,0,0), (0.5,0.5,0.5)], spacegroup=225, cellpar=cellpar)
atoms.calc = EMT()

print(len(atoms))
print(atoms.get_chemical_symbols())

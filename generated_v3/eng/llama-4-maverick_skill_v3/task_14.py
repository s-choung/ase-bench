from ase.spacegroup import crystal
from ase import Atoms

atoms = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, 
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

print(len(atoms))
print(atoms.get_chemical_symbols())

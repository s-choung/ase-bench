from ase.spacegroup import crystal
from ase import Atoms
import numpy as np

a = 5.64
atoms = crystal(['Na', 'Cl'], [(0,0,0), (0.5,0.5,0.5)],
                spacegroup=225, cellpar=[a, a, a, 90, 90, 90])

print(len(atoms))
print(atoms.get_chemical_symbols())

from ase import Atoms
from ase.spacegroup import crystal

a = 5.64
cell = a * [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
atoms = crystal(['Na', 'Cl'], [(0,0,0), (0.5,0.5,0.5)], spacegroup=225, cellpar=[a, a, a, 90, 90, 90])
print(len(atoms), atoms.get_chemical_formula())

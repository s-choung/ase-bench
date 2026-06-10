from ase import Atoms, Spacegroup
from ase.lattice.spacegroup import crystal
a = 5.64
sg = Spacegroup(225)
NaCl = crystal(['Na', 'Cl'], basis=[(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=sg, cellpar=[a, a, a, 90, 90, 90])
print(len(NaCl), NaCl.get_chemical_symbols())

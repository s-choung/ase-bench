from ase import Atoms
from ase.spacegroup import crystal

nacl = crystal(['Na', 'Cl'], 
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

print(len(nacl))
print(nacl.get_chemical_symbols())

from ase.spacegroup import crystal
from ase.calculators.emt import EMT

a = 5.64
nacl = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cell=a)
nacl.calc = EMT()

print(f"Number of atoms: {len(nacl)}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")

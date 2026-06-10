from ase import Atoms
from ase.spacegroup import crystal
from ase.data import atomic_numbers

a = 5.64
symbols = ['Na', 'Cl']
indices = [(0, 0, 0), (0.5, 0.5, 0.5)]

atoms = crystal('NaCl',
                positions=indices,
                spacegroup=225,
                cell=[a, a, a],
                symbol=symbols)

print(len(atoms))
print(atoms.get_symbols())

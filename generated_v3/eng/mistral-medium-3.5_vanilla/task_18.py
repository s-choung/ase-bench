from ase import Atoms
from ase.databases.g2 import G2
from ase.ga.utilities import get_all_bond_lengths

mol = G2('CH4')
print('Chemical formula:', mol.get_chemical_formula())
print('Atomic coordinates:')
for atom in mol:
    print(atom.symbol, atom.position)
print('Bond lengths [Å]:', get_all_bond_lengths(mol))

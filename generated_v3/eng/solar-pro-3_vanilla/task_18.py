from ase.g2 import G2NR
from ase.calculators.EMT import EMT
from ase.units import Bohr

mol = G2NR('CH4')

mol.set_calculator(EMT())
info = mol.get_molecular_properties()
bond_lengths = mol.get_distances()

print('Coordinates  (A, Bohr):')
print(mol.get_positions() * Bohr)
print('Bond lengths (A, Bohr):')
print(bond_lengths)
print('Formula:', mol.get_chemical_formula())

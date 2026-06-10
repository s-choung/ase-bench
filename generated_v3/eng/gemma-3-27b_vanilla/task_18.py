from ase.db import G2
from ase.calculators.emt import EMT
from ase.constraints import FixedAtoms
import numpy as np

mol = G2('methane')

print("Atomic coordinates:")
print(mol.get_positions())

print("\nChemical formula:")
print(mol.get_chemical_formula())

lengths = []
for i in range(mol.get_number_of_atoms()):
    for j in range(i + 1, mol.get_number_of_atoms()):
        lengths.append(np.linalg.norm(mol.get_positions()[i] - mol.get_positions()[j]))

print("\nBond lengths (Angstroms):")
print(lengths)

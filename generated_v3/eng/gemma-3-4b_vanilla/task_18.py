from ase import Atoms
from ase.io import read

try:
    ch4 = Atoms.get('G2:CH4')
    print("Atomic Coordinates:", ch4.positions)
    print("Bond Lengths:", ch4.get_longest_bond_length())
    print("Chemical Formula:", ch4.formula)
except Exception as e:
    print(f"Error retrieving CH4: {e}")

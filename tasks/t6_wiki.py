"""T6 Wiki: Write/read structure in VASP POSCAR format"""
from ase.build import bulk
from ase.io import read, write
import numpy as np

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
write('POSCAR', cu, format='vasp')
atoms_back = read('POSCAR', format='vasp')
print(f"Written and read back: {atoms_back.get_chemical_symbols()}")
print(f"Cell preserved: {np.allclose(cu.get_cell(), atoms_back.get_cell())}")
print(f"PBC: {atoms_back.get_pbc()}")
import os; os.remove('POSCAR')

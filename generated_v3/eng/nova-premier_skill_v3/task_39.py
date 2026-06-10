from ase import Atoms
from ase.build import bulk
from ase.io import write, read

au = bulk('Au','fcc'); write('au.xyz', au)
atoms = read('au.xyz')
print(", ".join(atoms.get_chemical_symbols()))
print(atoms.positions)
